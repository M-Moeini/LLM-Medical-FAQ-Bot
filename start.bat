@echo off
start /B uvicorn app:app --host 0.0.0.0 --port 8001 --reload
start python telegram_bot.py
