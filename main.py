from fastapi import FastAPI
import random

app = FastAPI()


@app.get('/helloworld')
async def root():
    return {'message': 'Hello World'}



