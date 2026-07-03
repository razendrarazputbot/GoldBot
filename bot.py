from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Gold Bot is Active!")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    app.run_polling()