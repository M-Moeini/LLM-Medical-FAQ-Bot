# Medical FAQ Bot

## Overview

This repository contains the source code for a **Medical FAQ Bot**, which answers medical questions using OpenAI's GPT-3.5 API and Telegram Bot API. The bot can respond to users' medical queries via both a FastAPI web interface and a Telegram chat interface.

The bot is **running on an AWS EC2 instance** and is currently in its **prototype phase**, meaning it’s not yet a full MVP but serves as a fair proof of concept for answering medical-related queries.

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

5. **MLOps Pipeline**: The bot uses basic **MLOps techniques**, integrating OpenAI’s GPT models and ensuring an automated flow for handling medical inquiries. While this prototype doesn't yet have a fully developed MLOps stack, the potential for building one (with monitoring, retraining models, version control for ML models, etc.) is essential for scaling this type of application.

## Features

- **FastAPI API** to allow HTTP-based querying of medical questions.
- **Telegram Bot Integration** for real-time querying by users.
- **Preprocessing of user input** to handle tokenization and stopword removal using **NLTK**.
- **Medical Terms Dataset Filtering** to restrict answers to relevant medical queries (Note: This is an early-stage approach and can be further enhanced with better NLP techniques).
- **LangChain for conversation management**, allowing smoother and more contextually-aware conversations with users.
- **MLOps Considerations**: The prototype includes a basic MLOps mindset, with model calls to OpenAI’s API, and an architecture designed for scale in the future.


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
