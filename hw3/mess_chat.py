from json import JSONDecodeError
from math import prod
from fastapi import FastAPI, Request, Response
from rmq import Producer
from rmq import Consumer
from logger import Logger
import requests

def chat_message_callback(channel, method, properties, body):
    #   Callback should append messages to a dictionary that can be returned to the user on request
    chats[len(chats)+1] = body.decode('utf-8')

chats = {}
app = FastAPI()
chat_log = Logger("chat")
chat_log("[*] Starting chat app ... ")

@app.get("/")
async def root():
    default_response = {'message': "You've hit Zac's API root endpoint"}
    return default_response

@app.post("/send/")
async def send(message: str):
    producer = Producer()
    producer(message)
    return {"result": "ENQUEUED"}

@app.get('/messages/')
async def messages():
    consumer = Consumer(callback=chat_message_callback)
    consumer.get_messages()
    return chats