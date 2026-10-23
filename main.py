from fastapi import FastAPI
import ollama

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API ativa"}

@app.post("/chat")
def chat(prompt: str):
    response = ollama.chat(model='llama3.2', messages=[
        {'role': 'user', 'content': prompt}
    ])
    return {"resposta": response['message']['content']}