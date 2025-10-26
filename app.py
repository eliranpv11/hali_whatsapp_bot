# -*- coding: utf-8 -*-
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

# קבלת המפתח מהסביבה (.env)
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body")
    sender = request.form.get("From")

    # 💅 הגדרת האישיות של חלי
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "את חלי, בונת ציפורניים מקצועית, חמה, מצחיקה ואדיבה. דברי בשפה טבעית ומזמינה עם כל לקוחה, כאילו היא חברה שלך שמגיעה לטיפוח ופינוק."
            },
            {"role": "user", "content": incoming_msg}
        ]
    )

    reply = response.choices[0].message["content"]

    twilio_resp = MessagingResponse()
    twilio_resp.message(reply)
    return str(twilio_resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
