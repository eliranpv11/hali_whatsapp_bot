from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    incoming_msg = request.values.get("Body", "").strip().lower()
    sender = request.values.get("From", "")

    print(f"📩 הודעה התקבלה מ-{sender}: {incoming_msg}")

    resp = MessagingResponse()
    msg = resp.message()

    # תגובות חכמות לפי תוכן ההודעה
    if "תור" in incoming_msg or "קביעת תור" in incoming_msg:
        msg.body("מושלם! 🥰 מתי נוח לך להגיע? תאריך ושעה ואני פה 💅")
    elif "מחיר" in incoming_msg or "מחירים" in incoming_msg:
        msg.body(
            "✨ מחירים ✨\n"
            "מניקור קלאסי – 70 ₪\n"
            "לק ג'ל – 120 ₪\n"
            "בניית ציפורניים – 200 ₪\n"
            "עיצוב אישי – בתיאום 💎\n\n"
            "אם יש שאלה – אני כאן בשבילך ❤️"
        )
    elif "היי" in incoming_msg or "שלום" in incoming_msg:
        msg.body("שלום מהממת! 💖 אני חלי, מניקוריסטית שמגשימה ציפורניים חלומיות ✨ איך אפשר לעזור?")
    else:
        msg.body("תודה שפנית אליי! 🌸 אני פה לשאלות, מחירים או קביעת תורים 💅")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
