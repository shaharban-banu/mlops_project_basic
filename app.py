from fastapi import FastAPI
import pickle
import numpy as np

app=FastAPI()

model=pickle.load(open("modelbasic.pkl","rb"))

@app.get('/predict')
def predict(age:int,salary:int):
    pred=model.predict([[age,salary]])
    return {'predcition':int(pred[0])}

