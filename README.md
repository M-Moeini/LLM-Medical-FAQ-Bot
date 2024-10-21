# Medical FAQ Bot

## Overview

This repository contains the source code for a **Medical FAQ Bot**, which answers medical questions using OpenAI's GPT-3.5 API and Telegram Bot API. The bot can respond to users' medical queries via both a FastAPI web interface and a Telegram chat interface.
The bot is **running on an AWS EC2 instance** and is currently in its **prototype phase**, meaning it’s not yet a full MVP but serves as a fair proof of concept for answering medical-related queries.

[![Medical Bot FAQ Preview](https://github.com/M-Moeini/LLM-Medical-FAQ-Bot/blob/main/medicalbotimg.webp)](https://github.com/M-Moeini/LLM-Medical-FAQ-Bot/issues/2)

## Tech Stack
- **Backend**: FastAPI
- **Telegram Bot**: Python Telegram Bot
- **OpenAI GPT-3.5** for answering medical questions
- **LangChain**: For managing interactions with OpenAI's GPT model
- **NLP Preprocessing**: NLTK
- **Medical Terms Dataset**: Custom CSV-based dataset for filtering questions
- **Hosting**: AWS EC2 with Dockerized application


## How It Works

1. **Telegram Bot Integration**: Users interact with the bot via Telegram. Upon receiving a question, the bot preprocesses the text using NLTK, identifies whether it is a medical question using a custom medical terms dataset, and either responds with a relevant answer or notifies the user if their query falls outside its scope.
   
2. **FastAPI Interface**: The bot also exposes an API endpoint using FastAPI. You can post a medical question to `/ask` in JSON format, and the bot will respond with an answer using the OpenAI GPT-3.5 engine.

3. **Medical Terms Filter**: The bot limits its responses to medical questions by checking if the user's query contains any words from a predefined list of medical terms. If no medical terms are found, the bot informs the user that it can only answer medical-related queries. While this approach is functional, it’s not the best practice for determining the context of a query. Advanced Natural Language Processing (NLP) techniques, such as **sentiment analysis** or **topic modeling**, could provide more accurate results.

4. **LangChain Integration**: The bot integrates **LangChain**, a framework for building applications powered by large language models (LLMs). It enables handling the conversational flow and interacting with GPT-3.5 through the **ConversationChain** class, allowing the bot to respond fluidly to medical questions.


## Features

- **FastAPI API** to allow HTTP-based querying of medical questions.
- **Telegram Bot Integration** for real-time querying by users.
- **Preprocessing of user input** to handle tokenization and stopword removal using **NLTK**.
- **Medical Terms Dataset Filtering** to restrict answers to relevant medical queries (Note: This is an early-stage approach and can be further enhanced with better NLP techniques).
- **LangChain for conversation management**, allowing smoother and more contextually-aware conversations with users.


## Setup & Running

### Prerequisites

- **Python 3.9**
- **AWS EC2 Instance**
- **Docker**

### Steps to Run Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/M-Moeini/LLM-Medical-FAQ-Bot.git
   cd LLM-Medical-FAQ-Bot


2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   

3. **Set Environment Variables**:
   **TELEGRAM_TOKEN**: Your Telegram bot token (You can get it from @BotFather in Telegram.)
   **OPENAI_API_KEY**: Your OpenAI API key (You can get it from openAI Website.)

4. **Run the Application**:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8001 & python telegram_bot.py

5. **Access it**:

The FastAPI app is accessible at:
```
http://<your-ec2-public-ip>:8001/ask
```

The Telegram bot can be interacted with via Telegram if you set it up with @BotFather.




### Steps to Run it on AWS EC2

Use the following command to copy your project files to the EC2 instance:

1. **Copy the files**:
```bash
scp -i your-key.pem -r /path/to/your/project ec2-user@your-ec2-public-ip:/home/ec2-user
```

2. **Build and Run Docker Container**:
Navigate to the project directory on your EC2 instance and run the following commands:

```bash
docker build -t medical_bot .
docker run -d -e TELEGRAM_TOKEN=<your_telegram_token> -e OPENAI_API_KEY=<your_openai_key> -p 8001:8001 medical_bot
```

3. **Access it**:

The FastAPI app is accessible at:
```
http://<your-ec2-public-ip>:8001/ask
```

The Telegram bot can be interacted with via Telegram if you set it up with @BotFather.


## Future Improvements

### Advanced NLP Techniques

Replacing the simple keyword-based approach for filtering medical queries with more sophisticated NLP techniques such as sentiment analysis, topic modeling, or intent detection.

### Full MLOps Pipeline

Currently, this prototype uses a minimal MLOps stack with the help of **Docker**. Future iterations could include:

- **Model versioning** to track the performance of different versions of the model.
- **Automatic retraining** based on feedback or new data.
- **Monitoring and alerting** to ensure smooth operation of the model in production.

### Cloud Development
   Running it on **AWS ElasticBeans** or running it with the help of **AWS Fargate + AWS ECS**


## Contribution
Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Contact
- **Mahdi Moeini**
  - **Email**: [mmoeini@mun.ca](mailto:mmoeini@mun.ca)
  - **LinkedIn**: [linkedin.com/in/mmoeini](https://linkedin.com/in/mmoeini)
  - **GitHub**: [m-moeini.github.io](https://m-moeini.github.io)


   
