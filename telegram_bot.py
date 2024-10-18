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
import pandas as pd

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')


telegram_token_path = r'F:\Job\Projects\Medical Bot\api_keys\telegram_token.text'
with open(telegram_token_path, 'r') as file:
    TELEGRAM_TOKEN = file.read().strip()  

api_key_path = r'F:\Job\Projects\Medical Bot\api_keys\key.text'
with open(api_key_path, 'r') as file:
    api_key = file.read().strip()  

FASTAPI_URL = "http://127.0.0.1:8000/ask"


conversation_chain = ConversationChain(
    llm=ChatOpenAI(temperature=0.7, openai_api_key=api_key)
)

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)



def load_medical_keywords(file_path):
    try:
        df = pd.read_csv(file_path)
        return df['keyword'].tolist()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    
MEDICAL_KEYWORDS = load_medical_keywords('F:\Job\Projects\Medical Bot\LLM-Medical-FAQ-Bot\medical_terms.csv')

# Preprocessing function using NLTK
def preprocess_question(question):
    tokens = word_tokenize(question)
    tokens = [word for word in tokens if word.isalnum()]  # Keep only alphanumeric tokens
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]  # Remove stopwords
    return " ".join(tokens)



async def start(update: Update, context):
    await update.message.reply_text("Hi! I'm your Medical FAQ Bot. Ask me a medical question!")


async def handle_message(update: Update, context):
    user_question = preprocess_question(update.message.text)

    # Check if the user's question contains any medical keywords
    # if any(keyword in user_question.lower() for keyword in MEDICAL_KEYWORDS):
    #     prompt = f"You are a medical assistant. Answer the following medical question: {user_question}"
    #     response = conversation_chain.run(input=prompt)
    # else:
    #     response = "I'm sorry, but I can only answer medical questions."
    response = conversation_chain.run(input=user_question)
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