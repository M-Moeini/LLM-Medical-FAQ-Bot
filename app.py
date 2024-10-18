from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
import openai
import os
file_path = '/home/mahdi146/projects/def-b09sdp/mahdi146/api-key/key.text'
with open(file_path, 'r') as file:
    api_key = file.read().strip()  

class Question(BaseModel):
    question: str

app = FastAPI()
openai.api_key = api_key
print('hi')
@app.get("/")
def read_root():
    print('there')
    return {"message": "Medical Bot is running"}




@app.post("/ask")
async def ask_openai(question: Question):  # Expecting a JSON body
    try:
        # Call the OpenAI Chat API to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or use "gpt-4" if you have access
            messages=[{"role": "user", "content": question.question}]  # Set up the message format
        )
        return {"answer": response.choices[0].message['content'].strip()}
    except Exception as e:
        return {"error": str(e)}