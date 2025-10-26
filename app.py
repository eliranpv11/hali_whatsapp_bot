# -*- coding: utf-8 -*-
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI
from dotenv import load_dotenv
from collections import defaultdict, deque
import os
import time

# טוען מפתח מה-.env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ===== הגדרות =====
MODEL = "gpt-4o"          # לא זול. לטסט זול יותר: "gpt-4o-mini"
MAX_TURNS = 15            # כמה הודעות נזכור לכל משתמש (קצר-טווח)
SYSTEM_PERSONA = (
    "את חלי – בונת ציפורניים מקצועית, חמה, מצחיקה ואדיבה. "
    "את מדברת עברית טבעית, קלילה ונעימה, עם אמפתיה ודיוק מקצועי. "
    "תחומי ידע: מניקור, פדיקור, בנייה, ג'ל, פרנץ', עיצובים, צבעים, חומרים, תחזוקה. "
    "בבקשות תורים: שאלת המשך ברורה (יום מועדף, בוקר/ערב), הצעת חלופות אם אין. "
    "שמרי תשובות קצרות, מעשיות וידידותיות; אפשר אמוג'י מדי פעם (לא להציף). "
    "אם משהו לא ברור – בקשי הבהרה בנימוס. "
    "אין לתת ייעוץ רפואי; במקרה כזה להמליץ לפנות למקצועית מתאימה."
)

# ===== זיכרון שיחות: לכל שולח נשמור תור היסטוריה =====
SESSIONS: dict[str, deque] = defaultdict(lambda: deque(maxlen=MAX_TURNS))

app = Flask(__name__)

def build_messages(sender: str, user_text: str):
    """
    בונה את רשימת ההודעות למודל: system + היסטוריה + הודעת המשתמש.
    """
    history = list(SESSIONS[sender])  # [(role, content), ...]
    msgs = [{"role": "system", "content": SYSTEM_PERSONA}]
    for role, content in history:
        msgs.append({"role": role, "content": content})
    msgs.append({"role": "user", "content": user_text})
    return msgs

def remember(sender: str, role: str, content: str):
    """
    מוסיף הודעה לזיכרון של המשתמש (קצר-טווח).
    """
    SESSIONS[sender].append((role, content))

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    start = time.time()
    incoming_msg = (request.form.get("Body") or "").strip()
    sender = request.form.get("From") or "unknown"

    tw = MessagingResponse()

    # אין טקסט? נחזיר הודעה קצרה
    if not incoming_msg:
        tw.message("אני כאן 💅 מה תרצי לשאול או לקבוע?")
        return str(tw)

    # פקודת איפוס ידנית
    if incoming_msg in {"איפוס", "reset", "נקה", " /reset"}:
        SESSIONS.pop(sender, None)
        tw.message("ניקיתי את השיחה ואיפסתי זיכרון 🧼 אפשר להמשיך מאפס!")
        return str(tw)

    try:
        # בונה הקשר עם הזיכרון
        messages = build_messages(sender, incoming_msg)

        # קריאה ל-GPT
        completion = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.8,
            max_tokens=350,
        )

        # חילוץ תשובה (תואם לגרסאות שונות)
        try:
            reply = completion.choices[0].message.content
        except AttributeError:
            reply = completion.choices[0].message["content"]

        # שומר זיכרון (הודעת משתמש + תשובת הבוט)
        remember(sender, "user", incoming_msg)
        remember(sender, "assistant", reply)

        tw.message(reply)
        return str(tw)

    except Exception as e:
        # לוג למסוף + תשובת fallback ללקוחה
        print("❌ ERROR:", repr(e))
        tw.message(
            "אופס, הייתה תקלה קטנה רגעית ואני על זה 🛠️. "
            "אפשר לנסות שוב בעוד דקה או לכתוב לי מה נוח לך לתור (יום ושעה) ואחזור עם אישור."
        )
        return str(tw), 200  # מחזירים 200 כדי שטוויליו לא ינסה שוב אוטומטית

if __name__ == "__main__":
    # לריצה מקומית + ngrok
    app.run(host="0.0.0.0", port=5000)
