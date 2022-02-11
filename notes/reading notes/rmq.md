# RabbitMQ

This will have a simple hello world producer consumer implimentation in Python as a tutorial for RabbitMQ. There is a docker image available at

```bash
docker pull rabbitmq
```

or run and download images on the fly

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

## Basics

RabbitMQ is a message broker that accepts and forwards messages.  
It accepts, stores, and forwards binary blobs of data (messages)

**Producer**: A program that sends messages is a producer  
**Consumer**: A program that waits to recieve messages
**Queue**: Main data structure. Each channel is a queue of messages that can be subscribed to by consumers  

Messages are never sent right to the queue, they have to go through exchanges first

Pika Python module is used for this tutorial. This tutorial uses AMQP 0-9-1, which is an open, general-purpose protocol for messaging

## Producers

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange="",
                      routing_key='hello',
                      body="Hello, world!")
print("[x] Sent message to the queue")
connection.close()
```

Produces should have methods to create and send different types of messages.

It is important to declare a queue to write to in order for consumers to subscribe to them

* Consumers will declare the queue again for redundancy which will not create duplicate queues

## Consumers

```python
import sys
import os
import pika

def callback(channel, method, properties, body):
    print(f"[+] Recieved: {body}")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare('hello')

    #   Queue must exists before trying to consume
    channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)
    print('[*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Stopping consumer ...")
        try: 
            sys.exit(0)
        except SystemExit:
            os._exit(0)
```

THe first step is always to make a channel subscribe, or declare, a queue to pull from

* The command ```channel.queue_declare(queue='hello')``` will create a queue if none already exists with that name

Consumers have to subscribe a callback function to a queue

Consumers can also acknowledge message consumption with the ack methods. Since auto_ack is set the true then it wil handle it for you

## Testing ideas

* Test that consumer can consume large volumes of messages built up in the queue
