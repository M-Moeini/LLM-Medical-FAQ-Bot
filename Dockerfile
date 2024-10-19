# Dockerfile
FROM python:3.9

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy all your application code
COPY . .

# Expose the FastAPI port (8001) for the FastAPI app
EXPOSE 8001

# Command to run both FastAPI app and Telegram bot
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8001 & python telegram_bot.py"]
