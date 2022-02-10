from json import JSONDecodeError
import webbrowser
from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.get("/")
async def root(req: Request, res: Response):
    default_response = {'message': 'Hello, World!'}
    
    try:
        body = await req.json()
        if body.message == None:
            return default_response
        elif body.message == "":
            return default_response
        else:
            res.
            return {'message': body.message}
    except JSONDecodeError:
        return default_response

@app.post("/send/")
async def root(req: Request):
    try:
        body = await req.json()
        webbrowser.open(body)
        return body
    except JSONDecodeError:
        return {"Error": "Unexpected error trying to recieve message"}