from json import JSONDecodeError
from fastapi import FastAPI, Request, Response
from rmq import Producer
from rmq import Consumer
from logger import Logger
import requests
import pika

chats = {}
app = FastAPI()
chat_log = Logger("chat")
chat_log("[*] Starting chat app ... ")

async def chat_message_callback(channel, method, properties, body):
    #   Callback should append messages to a dictionary that can be returned to the user on request
    chats[len(chats)+1] = body.decode('utf-8')

@app.get("/")
async def root():
    default_response = {'message': "You've hit Zac's API root endpoint"}
    return default_response

@app.post("/send/")
async def send(message: str):
    try:
        producer = Producer()
        producer(message)
        return {"result": "ENQUEUED MESSAGE"}
    except pika.exceptions.AMQPConnectionError:
        chat_log("[-] Unable to connect to RMQ server. Ensure connection string is correct, or test image is running")
        return {'result': 'MESSAGE_DROPPED', 'reason': 'Could not connect to RMQ server. Ensure connection string is correct, or test image is running'}

@app.get('/messages/')
async def messages():
    try:
        consumer = Consumer()
        consumer()
    except pika.exceptions.AMQPConnectionError:
        chat_log("[-] Unable to connect to RMQ server. Ensure connection string is correct, or test image is running")
    return chats