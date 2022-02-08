from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {'message': 'Hello, World!'}

@app.post("/")
async def put_root(message):
    return {'message': message}

@app.post("/send/")
async def root(sender: str, message: str):
    print (f"Sender: {sender}\nMessage: {message}")
    return {"sender": sender, 'message': message}