from ast import Import
import json
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello_root():
    return {"message": "hello xoka"}