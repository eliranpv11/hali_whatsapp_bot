# -*- coding: utf-8 -*-
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI
import os
from dotenv import load_dotenv

# טען את משתני הסביבה (כדי שנוכל להשתמש במפתח API בצורה מאובטחת)
load_dotenv()

# חיבור ל-OpenAI עם מפתח מתוך משתני סביבה
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# יצירת אפליקציית Flask
app = Flask(__name__)

# מסלול ברירת מחדל לבדיקה שהשרת פעיל
@app.route("/", methods=["GET"])
def home():
    return "✅ Hali WhatsApp Bot is running!"

# מסלול לקבלת הודעות מ-WhatsApp
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    # שליפת תוכן ההודעה ומספר השולח
    incoming_msg = request.form.get("Body", "").strip()
    from_number = request.form.get("From", "")
    print(f"📩 התקבלה הודעה מ-{from_number}: {incoming_msg}")

    try:
        # קריאה למודל GPT-4o-mini עם הנחיית מערכת קבועה
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
        print(f"❌ שגיאה מול OpenAI: {e}")
        ai_reply = "מצטערת, הייתה תקלה זמנית. נסה שוב עוד רגע."

    print(f"💬 תשובה שנשלחה ל-{from_number}: {ai_reply}")

    # יצירת תגובה ל-Twilio
    twilio_resp = MessagingResponse()
    twilio_resp.message(ai_reply)
    return str(twilio_resp)

# הפעלת השרת באופן מקומי (לצורך בדיקות בלבד)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
