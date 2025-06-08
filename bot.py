import os

import openai
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = os.environ.get("BOT_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой бот.")
    context.chat_data["messages"] = []


async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.chat_data.clear()
    await update.message.reply_text("Диалог сброшен")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or update.message.text is None:
        return

    user_msg = update.message.text
    history = context.chat_data.setdefault("messages", [])
    history.append({"role": "user", "content": user_msg})

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=history,
        )
        bot_msg = response.choices[0].message.content.strip()
        history.append({"role": "assistant", "content": bot_msg})
    except Exception as e:  # pragma: no cover - network failure
        bot_msg = f"Ошибка при обращении к AI: {e}"

    await update.message.reply_text(bot_msg)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()