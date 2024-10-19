from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
import openai
import os

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")



class Question(BaseModel):
    question: str

app = FastAPI()
openai.api_key = api_key
@app.get("/")
def read_root():
    print('there')
    return {"message": "Medical Bot is running"}




@app.post("/ask")
async def ask_openai(question: Question):
    try:
        # Call the OpenAI Chat API to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": question.question}] 
        )
        return {"answer": response.choices[0].message['content'].strip()}
    except Exception as e:
        return {"error": str(e)}