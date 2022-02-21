# Messaging System

Requirements

* pika
* requests
* pytest
* fastapi
* logging

Uses 

Uses point-to-point venv for development environment
To activate:

```bash
point-to-point/Scripts/Activate.ps1
```

Docker Image for local testing

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

To run:

```bash
python -m uvicorn mess_chat:app --reload
```

This will run the application on <http://localhost:8000/>. The endpoints are ./send/{message} to send messages to the server and ./messages/ to retrieve the messages.
