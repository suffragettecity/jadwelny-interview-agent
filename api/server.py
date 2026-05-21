from fastapi import FastAPI, Request
from fastapi.responses import Response

from memory.conversation import get_history, clear_history, save_history
from agent.core import run_agent
from frontend.telegram import 

app = FastAPI(title="Jadwelny")

@app.get("/")
def root():
    return{"status": "running"}

async def webhook(request: Request):
    data = await request.json()
    
    message = data.get("message")
    chat_id = message["chat"]["id"]
    user_message = message.get("text", "")

    history = get_history(chat_id)
    reply = run_agent(user_message, history)
    save_history(chat_id, history)

    
