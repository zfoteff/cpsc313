from json import JSONDecodeError
from fastapi import FastAPI, Request, Response
from rmq import Producer
from rmq import Consumer
from logger import Logger
import requests

app = FastAPI()
chat_log = Logger("chat")

@app.get("/")
async def root():
    default_response = {'message': "You've hit Zac's API root endpoint"}
    return default_response

@app.post("/send/")
async def send(message: str):
    return {"message": message}

@app.get('/messages/')
async def messages():
    #message_results = Consumer()
    return {
            "messages": {
                1: "message 1",
                2: "message 2",
                3: "message 3",
                4: "message 4",
                5: "message 5"
            }}