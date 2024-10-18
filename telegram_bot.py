import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import requests
import asyncio
import os
file_path = '/home/mahdi146/projects/def-b09sdp/mahdi146/api-key/telegram_token.text'
with open(file_path, 'r') as file:
    TELEGRAM_TOKEN = file.read().strip()  

FASTAPI_URL = "http://127.0.0.1:8000/ask"

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context):
    await update.message.reply_text("Hi! I'm your Medical FAQ Bot. Ask me a medical question!")

async def handle_message(update: Update, context):
    user_question = update.message.text
    response = requests.post(FASTAPI_URL, json={"question": user_question})
    bot_response = response.json().get("answer", "I couldn't find an answer. Please try again.")
    await update.message.reply_text(bot_response)

# Main function to run the bot
def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Message handler for all messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()