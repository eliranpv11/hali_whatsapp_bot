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
