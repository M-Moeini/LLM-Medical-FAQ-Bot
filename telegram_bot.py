import logging
import nltk
import requests
import asyncio
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain
from langchain_community.chat_models import ChatOpenAI
import nltk
print('ho')
print('ho')
# nltk.download('punkt')
# nltk.download('stopwords')

file_path = '/home/mahdi146/projects/def-b09sdp/mahdi146/api-key/telegram_token.text'
with open(file_path, 'r') as file:
    TELEGRAM_TOKEN = file.read().strip()  

FASTAPI_URL = "http://127.0.0.1:8000/ask"


conversation_chain = ConversationChain(
    llm=ChatOpenAI(temperature=0.7, openai_api_key="your-openai-api-key")
)
print('hi')
# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Preprocessing function using NLTK
def preprocess_question(question):
    tokens = word_tokenize(question)
    tokens = [word for word in tokens if word.isalnum()]  # Keep only alphanumeric tokens
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]  # Remove stopwords
    return " ".join(tokens)



async def start(update: Update, context):
    await update.message.reply_text("Hi! I'm your Medical FAQ Bot. Ask me a medical question!")

# async def handle_message(update: Update, context):
#     user_question = update.message.text
#     response = requests.post(FASTAPI_URL, json={"question": user_question})
#     bot_response = response.json().get("answer", "I couldn't find an answer. Please try again.")
#     await update.message.reply_text(bot_response)

async def handle_message(update: Update, context):
    user_question = preprocess_question(update.message.text)
    
    # Optionally use Langchain for conversation management
    response = conversation_chain.run(input=user_question)
    
    # If you prefer calling FastAPI and OpenAI directly:
    # response = requests.post(FASTAPI_URL, json={"question": user_question})
    # bot_response = response.json().get("answer", "I couldn't find an answer. Please try again.")
    
    await update.message.reply_text(response)


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