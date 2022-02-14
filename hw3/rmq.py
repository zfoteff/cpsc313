import sys
import pika
import time
from logger import Logger
from multiprocessing import Process
from pika.exchange_type import ExchangeType

producer_logger = Logger(key="producer")
consumer_logger = Logger(key="consumer")

#http://cps-devops.gonzaga.edu:5672
HOST_URL = "localhost"
EXCHANGE = ""
EXCHANGE_TYPE = ExchangeType.topic

class Producer:
    """
    Producer class for publishing messages to a queue
    """
    def __init__(self, host=HOST_URL, queue="general"):
        """
        Create new instance of consumer class

        Args:
            host ([type], optional): [description]. Defaults to HOST_URL.
            queue (str, optional): [description]. Defaults to "general".
        """
        self._host = host
        self.queue = queue
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(f"{self._host}"))
        producer_logger(f"[*] Created new producer on host {self._host} for queue {self.queue}")
    
    def __call__(self, message):
        message = message.encode('utf-8')
        channel = self.conn.channel()
        channel.queue_declare(queue=f"{self.queue}")
        channel.basic_publish(exchange=EXCHANGE, 
                              routing_key=self.queue, 
                              body=message)
        producer_logger(f"[+] Sent Message to queue {self.queue}")
        self.conn.close()
        
class Consumer:
    def default_callback(self, channel, method, properties, body):
        message = body.decode('utf-8')
        consumer_logger(f"[-] Consumed message {message} from the queue")
    
    def __init__(self, host=HOST_URL, topic="general", callback=default_callback):
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(f"{host}"))
        self.channel = self.conn.channel()
        self.channel.queue_declare(f"{topic}")
        self.channel.basic_consume(queue=topic, 
                                   auto_ack=True, 
                                   on_message_callback=callback)
        consumer_logger(f"[*] Created consumer on host {host} for queue {topic}")
        
    def get_messages(self):
        consumer_logger("[*] Listening for messages from queue")
        consumer_process = Process(target=self.channel.start_consuming(), name="consumer_process")
        consumer_process.start()
        consumer_process.join(timeout=1)
        consumer_process.terminate()

    def close_connection(self):
        self.conn.close()