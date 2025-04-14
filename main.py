from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import os

TOKEN = os.getenv("BOT_TOKEN")
MOT_SECRET = "lunevibrante"
REPONSE_SECRETE = "✨ Bravo ! Le chiffre est : 7 🌙"

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text.lower() == MOT_SECRET.lower():
        await update.message.reply_text(REPONSE_SECRETE)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
app.run_polling()
