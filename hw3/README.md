# Messaging System

Uses point-to-point venv  
To activate:

```bash
point-to-point/Scripts/Activate.ps1
```

To run:

```bash
python -m uvicorn mess_chat:app --reload
```

Docker Image for local testing
```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

Messaging server running rabbitmq
cps-devops  
Connection information forthcoming

