# -*- coding: utf-8 -*-
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI
import os
from dotenv import load_dotenv

# טוען משתני סביבה
load_dotenv()

# חיבור ל-OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body", "").strip()
    from_number = request.form.get("From", "")
    print(f"📩 התקבלה הודעה מ-{from_number}: {incoming_msg}")

    try:
        # תשובה מבינה מלאכותית
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "את העוזרת האישית חלי. דברי תמיד בעברית, בטון אישי, חמים ונעים, ועני בטבעיות."
                },
                {"role": "user", "content": incoming_msg}
            ]
        )
        ai_reply = completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ שגיאה: {e}")
        ai_reply = "מצטערת, אירעה תקלה זמנית. נסה שוב מאוחר יותר."

    print(f"💬 תשובה שנשלחה ל-{from_number}: {ai_reply}")

    twilio_resp = MessagingResponse()
    twilio_resp.message(ai_reply)
    return str(twilio_resp)

@app.route("/", methods=["GET"])
def home():
    return "✅ Hali WhatsApp Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
