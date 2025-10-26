# -*- coding: utf-8 -*-
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

# טעינת המפתחות מה-.env
load_dotenv()

# חיבור ל-OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# רק משתנים שקשורים לוואטסאפ
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

app = Flask(__name__)

# אישיות של הבוט
SYSTEM_PERSONA = (
    "את חלי 💅 – בונת ציפורניים מקצועית עם ניסיון של כמעט שלוש שנים בלבד. "
    "תמיד תצייני 'כמעט שלוש שנים' – לעולם לא יותר. "
    "את חמה, מצחיקה וקלילה, עם כלבה מתוקה בשם ג׳וי 🐶. "
    "כשלקוחות מתלבטות לגבי צבעים או עיצובים – תסבירי בהתלהבות ועם המלצה אישית. "
    "תדברי עברית טבעית, קלילה ונעימה, עם אמוג׳ים עדינים 💅✨🌸🐾."
)

# Webhook של וואטסאפ
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = (request.form.get("Body") or "").strip()
    sender = request.form.get("From") or "unknown"

    print(f"💬 הודעה מוואטסאפ ({sender}): {incoming_msg}")

    # הגדרת תשובה לבוט
    tw = MessagingResponse()

    if not incoming_msg:
        tw.message("אני כאן 💅 מה תרצי לשאול או לקבוע?")
        return str(tw)

    try:
        # שליחת ההודעה ל-OpenAI לקבלת תשובה
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

        # החזרת התשובה לוואטספ
        tw.message(reply)
        return str(tw)

    except Exception as e:
        print("❌ שגיאה בוואטסאפ:", e)
        tw.message("אופס, הייתה תקלה קטנה 💅 נסי שוב עוד רגע")
        return str(tw), 200


# הפעלת השרת
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
