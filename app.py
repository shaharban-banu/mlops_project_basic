from fastapi import FastAPI
import pickle
import numpy as np
import logging
import json

with open("config.json") as f:
    config=json.load(f)
PORT=config.get("port",8000)
MODEL_NAME=config.get("model","default_model")
MODEL_VERSION=config.get("version","1.0")

logging.basicConfig(level=logging.INFO,filename="app.log")

app=FastAPI()

model=pickle.load(open("modelbasic.pkl","rb"))

request_count=0

@app.get("/")
def home():
    return {
        "message": "ML API Running 🚀",
        "model": MODEL_NAME,
        "version": MODEL_VERSION
    }


@app.get('/predict')
def predict(age:int,salary:int):
    global request_count
    request_count+=1
    pred=model.predict([[age,salary]])
    logging.info(f"request : {request_count} | input : {age},{salary} | prediction : {pred}")
    return {'predcition':int(pred[0])}

@app.get('/metrics')
def metrics():
    return {'total_requests':request_count}
@app.get('/health')
def health():
    return {'status':'ok'}
