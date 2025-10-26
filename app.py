# -*- coding: utf-8 -*-
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI
import os
from dotenv import load_dotenv

# טוען משתני סביבה
load_dotenv()

# התחברות ל-OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body")
    sender = request.form.get("From")

    # מדפיס ללוגים כדי לבדוק שההודעה מגיעה
    print(f"📩 התקבלה הודעה מ-{sender}: {incoming_msg}")

    try:
        # שליחת הבקשה ל-OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "אתה עוזר אישי נחמד שמשיב בעברית על שאלות המשתמש."
                },
                {"role": "user", "content": incoming_msg}
            ]
        )

        reply = response.choices[0].message.content
        print(f"💬 תשובה שנשלחה ל-{sender}: {reply}")

    except Exception as e:
        reply = "😕 חלה תקלה זמנית. נסה שוב עוד רגע."
        print(f"❌ שגיאה: {e}")

    # שליחת תגובה ל-Twilio
    twilio_resp = MessagingResponse()
    twilio_resp.message(reply)
    return str(twilio_resp)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
