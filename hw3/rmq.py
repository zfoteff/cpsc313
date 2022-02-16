import sys
import pika
import time
from logger import Logger

producer_logger = Logger(key="producer")
consumer_logger = Logger(key="consumer")

#http://cps-devops.gonzaga.edu:5672
HOST_URL = "amqp://guest:guest@localhost:5672/"
EXCHANGE = "messages"
EXCHANGE_TYPE = "fanout"
RMQ_PORT = "5672"
RMQ_DEFAULT_PUBLIC_QUEUE = "general"
RMQ_PRIVATE_QUEUE = "zfoteff"
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
        self.queue = queue
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(f"{host}"))
        producer_logger(f"[*] Created new producer on host {host} for queue {self.queue}")
    
    def __call__(self, message):
        message = message.encode('utf-8')
        channel = self.conn.channel()
        channel.queue_declare(queue=f"{self.queue}")
        channel.basic_publish(exchange=EXCHANGE, 
                              body=message)
        producer_logger(f"[+] Sent Message to queue {self.queue}: {message}")
        channel.close()
        
    def on_open():
        pass
        
class Consumer:
    def __init__(self, host=HOST_URL):
        self._connection = None
        self._channel = None
        self._closing = False
        self._consumer_tag = None
        self._queue = "general"
        self._url = host
        
    def __call__(self):
        self._connection = self.connect()
        self._connection.ioloop.start()
        
    def default_callback(self, channel, method, properties, body):
        message = body.decode('utf-8')
        consumer_logger(f"[-] Consumed message {message} from the queue")
        
    def setup_exchange(self, exchange_name):
        consumer_logger(f"[*] Declaring exchange {exchange_name} . . .")
        self._channel.exchange_declare(self.on_exchange_declared, exchange_name, EXCHANGE_TYPE)
    
    def setup_queue(self, queue_name):
        consumer_logger(f"[*] Declaring queue {queue_name} . . .")
        self._channel.queue_declare(self.on_queue_declared, queue_name)
    
    def on_exchange_declared(self, unused_frame):
        consumer_logger('[+] Exchange declared')
        self.setup_queue(self._queue)
        
    def on_queue_declared(self, unused_frame):
        consumer_logger(f'[+] Bound queue {self._queue} with exchange {EXCHANGE}')
        self._channel.queue_bind(self.start_consuming, self._queue, EXCHANGE)
    
    def start_consuming(self):
        consumer_logger(f"[*] Started consuming from queue {self._queue}")
        self._channel.add_on_cancel_callback(self.on_consumer_cancelled)
        self._consumer_tag = self._channel.basic_consume(self.on_message, self._queue)
        
    def stop_consuming(self):
        if self._channel:
            consumer_logger(f"[*] Stopping consumer . . .")
            if self._channel:                
                self._channel.basic_cancel(self._channel.close(), self._consumer_tag)
        
    def on_consumer_cancelled(self):
        consumer_logger(f"[-] Stopping consumer for queue {self._queue}")
        if self._channel:
            self._channel.close()
    
    def on_message(self, unused_channel, basic_deliver, properties, body):
        consumer_logger(f"[+] {basic_deliver.delivery_tag} RECIEVED MESSAGE: {body}")
        self._channel.basic_ack(basic_deliver.delivery_tag)
        
    def stop(self):
        self._closing = True
        self.stop_consuming()
        self._connection.ioloop.stop()
    
    def connect(self):
        consumer_logger(f"[*] Connecting to {self._url} . . .")
        return pika.SelectConnection(pika.URLParameters(self._url), 
                                     self.on_connection_open)
    
    def reconnect(self):
        self._connection.ioloop.stop()
        if not self._closing():
            #   Create new connection
            self._connection = self.connect()
            #   Create new ioloop to run the consumer on
            self._connection.ioloop.start()

    def on_connection_open(self, incoming_connection):
        consumer_logger(f"[+] Connected to {self._url}")
        #   Add closing callback
        self._connection.add_on_close_callback(self.on_connection_closed)
        self.open_channel()
        
    def on_connection_closed(self, connection, reply_code, reply_text):
        self._channel = None
        if self._closing:
            self._connection.ioloop.stop()
        else:
            consumer_logger(f"Connection closed, reopening in 5 seconds: {reply_code} {reply_text}")
            self._connection.add_timeout(5, self.reconnect)
        consumer_logger(f"[-] Closed connection to {self._url}")
                    
    def open_channel(self):
        consumer_logger(f"[*] Opening new channel to {self._url} . . .")
        self._connection.channel(on_open_callback=self.on_channel_open)
        
    def on_channel_open(self, channel):
        consumer_logger(f"[+] Opened new channel to {self._url}")
        self._channel = channel
        self._channel.add_on_close_callback(self.on_channel_closed)
        self.setup_exchange(EXCHANGE)

    def on_channel_closed(self, channel, reply_code, reply_text):
        consumer_logger(f"[-] Closed channel to {self._url}: {reply_code} {reply_text}")
        self._connection.close()
        
    