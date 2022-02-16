import pika

GET_ALL_MESSAGES = -1

class MessageServer():
    def __init__(self):
        pass
    
    def send_message(self, message: str, target_queue: str):
        pass
    
    def recieve_message(self, target_queue: str, num_messages: int = GET_ALL_MESSAGES):
        pass