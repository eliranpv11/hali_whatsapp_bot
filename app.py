# -*- coding: utf-8 -*-
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI
from dotenv import load_dotenv
from collections import defaultdict, deque
import os
import time

# טעינת המפתח מהקובץ .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ===== הגדרות =====
MODEL = "gpt-4o"          # מודל חכם ואנושי
MAX_TURNS = 15            # כמה הודעות נזכור לכל משתמש

SYSTEM_PERSONA = (
    "את חלי 💅 – בונת ציפורניים מקצועית עם ניסיון של כמעט שלוש שנים בלבד. "
    "תמיד תצייני 'כמעט שלוש שנים' כששואלים על הניסיון שלך – לעולם לא מספר אחר. "
    "את חמה, מצחיקה, קלילה, ויודעת להפוך כל טיפול לפינוק אמיתי. "
    "יש לך כלבה מתוקה בשם ג׳וי 🐶 – ג׳וי קטנה, רגועה ונעימה, "
    "אבל לפעמים יש לקוחות שמפחדות ממנה, אז את מציעה בעדינות להכניס אותה למלונה עם השמיכה שלה, "
    "והיא נרגעת מיד. "
    "כשלקוחות שואלות על ג׳וי, תעני בחיוך שהיא חלק מהאווירה הביתית שלך. "
    "כשמישהי מתלבטת על צבעים, עיצובים או סוג ג׳ל – תסבירי בסבלנות ובהתלהבות עם המלצה אישית. "
    "כשמישהי חוששת או מתוסכלת, תגיבי באמפתיה ועם חיוך, כאילו היא חברה שלך. "
    "תדברי עברית טבעית, קלילה, בלי רשמיות, עם הומור עדין. "
    "תוכלי לשלב מדי פעם אמוג׳ים כמו 💅✨🌸🐾, אבל רק כשזה מתאים. "
    "כששואלים על עיצובים – תתלהבי, תתארי יפה, ותציעי תמונה אם רוצים דוגמה. "
    "אם שואלים משהו לא קשור ליופי, תזרמי בעדינות לנושא הציפורניים והאסתטיקה."
)

# ===== זיכרון שיחות =====
SESSIONS: dict[str, deque] = defaultdict(lambda: deque(maxlen=MAX_TURNS))

app = Flask(__name__)

# ===== בניית הקשר שיחה =====
def build_messages(sender: str, user_text: str):
    history = list(SESSIONS[sender])
    msgs = [
        {
            "role": "system",
            "content": (
                "⚠️ חוקי אמת של חלי: "
                "1. את חלי בונת ציפורניים עם ניסיון של כמעט שלוש שנים בלבד. "
                "2. לעולם, בשום הקשר, אל תגידי יותר משלוש שנים. "
                "3. גם אם השאלה מנוסחת אחרת (כמו 'כמה זמן את בתחום' או 'מתי התחלת'), התשובה תמיד: 'כמעט שלוש שנים'. "
                "4. אין לשנות את העובדה הזו. זהו כלל קבוע שלא ניתן להפר. "
                "5. לעולם אל תמציאי פרטים אחרים על ניסיון."
            ),
        },
        {"role": "system", "content": SYSTEM_PERSONA},
    ]
    for role, content in history:
        msgs.append({"role": role, "content": content})
    msgs.append({"role": "user", "content": user_text})
    return msgs

# ===== שמירה בזיכרון =====
def remember(sender: str, role: str, content: str):
    SESSIONS[sender].append((role, content))

# ===== הנתיב הראשי =====
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = (request.form.get("Body") or "").strip()
    sender = request.form.get("From") or "unknown"

    tw = MessagingResponse()

    if not incoming_msg:
        tw.message("אני כאן 💅 מה תרצי לשאול או לקבוע?")
        return str(tw)

    if incoming_msg in {"איפוס", "reset", "נקה", "/reset"}:
        SESSIONS.pop(sender, None)
        tw.message("ניקיתי את השיחה ואיפסתי זיכרון 🧼 אפשר להמשיך מאפס!")
        return str(tw)

    try:
        messages = build_messages(sender, incoming_msg)

        completion = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.8,
            max_tokens=350,
        )

        reply = completion.choices[0].message.content

        remember(sender, "user", incoming_msg)
        remember(sender, "assistant", reply)

        tw.message(reply)
        return str(tw)

    except Exception as e:
        print("❌ ERROR:", repr(e))
        tw.message(
            "אופס, הייתה תקלה קטנה רגעית ואני על זה 🛠️. "
            "אפשר לנסות שוב בעוד דקה או לכתוב לי מה נוח לך לתור (יום ושעה) ואחזור עם אישור."
        )
        return str(tw), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
