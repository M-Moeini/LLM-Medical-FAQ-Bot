import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import requests
import os
file_path = '/home/mahdi146/projects/def-b09sdp/mahdi146/api-key/telegram_token.text'
with open(file_path, 'r') as file:
    TELEGRAM_TOKEN = file.read().strip()  

FASTAPI_URL = "http://127.0.0.1:8000/ask"
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
