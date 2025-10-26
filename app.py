# -*- coding: utf-8 -*-
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
                {"role": "system", "content": "אתה העוזרת האישית חלי, ענה תמיד בעברית, בטון אישי ונעים."},
                {"role": "user", "content": incoming_msg}
            ]
        )
        ai_reply = completion.choices[0].message.content.strip()
    except Exception as e:
        ai_reply = "מצטערת, אירעה תקלה זמנית. נסה שוב מאוחר יותר."

    print(f"💬 תשובה שנשלחה ל-{from_number}: {ai_reply}")

    # תשובה חזרה לוואטסאפ בלבד
    twilio_resp = MessagingResponse()
    twilio_resp.message(ai_reply)
    return str(twilio_resp)

@app.route("/", methods=["GET"])
def home():
    return "✅ Hali WhatsApp Bot is active and running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
