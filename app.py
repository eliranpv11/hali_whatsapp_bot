# -*- coding: utf-8 -*-
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

# טוען את המפתחות מה-.env
load_dotenv()

# התחברות לשירותים
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

app = Flask(__name__)

# ===== אישיות של חלי =====
SYSTEM_PERSONA = (
    "את חלי 💅 – בונת ציפורניים מקצועית עם ניסיון של כמעט שלוש שנים בלבד. "
    "תמיד תצייני 'כמעט שלוש שנים' – לעולם לא יותר. "
    "את חמה, מצחיקה וקלילה, עם כלבה מתוקה בשם ג׳וי 🐶. "
    "כשלקוחות מתלבטות לגבי צבעים או עיצובים – תסבירי בהתלהבות ועם המלצה אישית. "
    "תדברי עברית טבעית, קלילה ונעימה, עם אמוג׳ים עדינים 💅✨🌸🐾."
)

# ===== פונקציה לשליחת הודעה לטלגרם =====
def send_to_telegram(msg: str):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {"chat_id": TELEGRAM_CHAT_ID, "text": msg}
        requests.post(url, data=data)
    except Exception as e:
        print("❌ טעות בטלגרם:", e)

# ===== נקודת וואטסאפ =====
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = (request.form.get("Body") or "").strip()
    sender = request.form.get("From") or "unknown"

    print(f"💬 הודעה מ-{sender}: {incoming_msg}")
    send_to_telegram(f"💬 וואטסאפ ({sender}): {incoming_msg}")

    tw = MessagingResponse()

    if not incoming_msg:
        tw.message("אני כאן 💅 מה תרצי לשאול או לקבוע?")
        return str(tw)

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PERSONA},
                {"role": "user", "content": incoming_msg}
            ],
            temperature=0.8,
            max_tokens=300,
        )

        reply = completion.choices[0].message.content
        send_to_telegram(f"💅 תשובת חלי:\n{reply}")

        tw.message(reply)
        return str(tw)

    except Exception as e:
        print("❌ שגיאה:", e)
        send_to_telegram(f"⚠️ שגיאה בחלי: {e}")
        tw.message("אופס, הייתה תקלה קטנה 💅 נסי שוב עוד רגע")
        return str(tw), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
