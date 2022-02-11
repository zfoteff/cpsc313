import pika
import sys
import os
import requests
from logger import Logger

producer_logger = Logger("producer")
consumer_logger = Logger("consumer")

HOST_URL = ""

class Producer:
    def __init__(self, host, queue):
        self._host = host
        self.queue = queue
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(f"{self._host}"))
        producer_logger(f"Created new producer on host {self._host} for queue {self.queue}")
    
    def __call__(self, message):
        message = message.encode('utf-8')
        channel = self.conn.channel()
        channel.queue_declare(queue=f"{self.queue}")
        channel.basic_publish(exchange="", 
                              routing_key=self.queue, 
                              body=message)
        producer_logger("[+] Sent Message to queue {self.queue}")
        self.conn.close()
        
class Consumer:
    def default_callback(self, channel, method, properties, body):
        message = body.decode('utf-8')
        print(f"Recieved :=> {message}")
        consumer_logger(f"Consumed message {message} from the queue")
    
    def __init__(self, host, queue, callback=default_callback):
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(f"{host}"))
        self.channel = self.conn.channel()
        self.channel.queue_declare(f"{queue}")
        self.channel.basic_consume(queue=self.queue, 
                                   auto_ack=True, 
                                   on_message_callback=self.default_callback)
        consumer_logger(f"Created new producer on host {self._host} for queue {self.queue}")
        print(f"[*] Waiting for messages from queue {self.queue}")
        self.channel.start_consuming()
        
    def stop_consuming(self):
        self.channel.stop_consuming()
        print(f"[*] Stopped listening for messages from queue {self.queue}")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)