from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import json

ADMIN_ID = 5925170010  # ❗ замени на свой Telegram ID

def load_users():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(data):
    with open("users.json", "w") as f:
        json.dump(data, f)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    users = load_users()

    if update.message.chat_id == ADMIN_ID:
        if ":" in update.message.text:
            uid, msg = update.message.text.split(":", 1)
            users[uid]["reply"] = msg.strip()
            save_users(users)
            await update.message.reply_text("Ответ отправлен на сайт.")
    else:
        uid = str(update.message.chat_id)
        users[uid] = {"msg": update.message.text, "reply": ""}
        save_users(users)

        await context.bot.send_message(
            ADMIN_ID,
            f"Сообщение с сайта\nID: {uid}\nТекст: {update.message.text}\n\nОтветь так:\n{uid}: твой ответ"
        )

async def main():
    app = ApplicationBuilder().token("ТОКЕН_БОТА").build()
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
