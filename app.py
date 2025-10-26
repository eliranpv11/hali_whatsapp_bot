# -*- coding: utf-8 -*-
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

# ===== טעינת מפתחות מה-.env =====
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
HLI_CHAT_ID = os.getenv("HLI_CHAT_ID")  # Chat ID של חלי

app = Flask(__name__)

# ===== אישיות של חלי =====
SYSTEM_PERSONA = (
    "את חלי 💅 – בונת ציפורניים מקצועית עם ניסיון של כמעט שלוש שנים בלבד. "
    "תמיד תצייני 'כמעט שלוש שנים' – לעולם לא יותר. "
    "את חמה, מצחיקה וקלילה, עם כלבה מתוקה בשם ג׳וי 🐶. "
    "כשלקוחות מתלבטות לגבי צבעים או עיצובים – תסבירי בהתלהבות ועם המלצה אישית. "
    "תדברי עברית טבעית, קלילה ונעימה, עם אמוג׳ים עדינים 💅✨🌸🐾."
)

# ===== שליחת הודעה לטלגרם של חלי (למעקב בלבד) =====
def send_to_hali_telegram(msg: str):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {"chat_id": HLI_CHAT_ID, "text": msg}
        requests.post(url, data=data)
    except Exception as e:
        print("❌ טעות בטלגרם של חלי:", e)


# ==========================================================
# 🟢 1. נקודת וואטסאפ (Twilio Webhook)
# ==========================================================
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = (request.form.get("Body") or "").strip()
    sender = request.form.get("From") or "unknown"

    print(f"💬 הודעה מוואטסאפ ({sender}): {incoming_msg}")

    # שליחה גם לטלגרם של חלי (למעקב בלבד)
    send_to_hali_telegram(f"💬 וואטסאפ ({sender}): {incoming_msg}")

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

        # שליחה גם לטלגרם של חלי
        send_to_hali_telegram(f"💅 תשובת חלי (וואטסאפ):\n{reply}")

        tw.message(reply)
        return str(tw)

    except Exception as e:
        print("❌ שגיאה בוואטסאפ:", e)
        send_to_hali_telegram(f"⚠️ שגיאה בוואטסאפ: {e}")
        tw.message("אופס, הייתה תקלה קטנה 💅 נסי שוב עוד רגע")
        return str(tw), 200


# ==========================================================
# 🔵 2. נקודת טלגרם (Telegram Webhook)
# ==========================================================
@app.route("/telegram", methods=["POST"])
def telegram_reply():
    data = request.get_json()
    if not data or "message" not in data:
        return "no message", 200

    chat_id = data["message"]["chat"]["id"]
    incoming_msg = data["message"].get("text", "").strip()
    user_name = data["message"]["from"].get("first_name", "לא ידוע")

    print(f"💬 הודעה מטלגרם ({user_name} / {chat_id}): {incoming_msg}")

    if not incoming_msg:
        send_message_telegram(chat_id, "אני כאן 💅 מה תרצי לשאול או לקבוע?")
        return "ok", 200

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
        send_message_telegram(chat_id, reply)

    except Exception as e:
        print("❌ שגיאה בטלגרם:", e)
        send_message_telegram(chat_id, "אופס, הייתה תקלה קטנה 💅 נסי שוב עוד רגע")

    return "ok", 200


# ===== פונקציה כללית לשליחת הודעות למשתמשים בטלגרם =====
def send_message_telegram(chat_id, text):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": chat_id, "text": text})
    except Exception as e:
        print("❌ שגיאה בשליחת הודעה לטלגרם:", e)


# ==========================================================
# 🚀 הפעלת השרת
# ==========================================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
