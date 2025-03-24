from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd
app = FastAPI()
model = joblib.load('xgboost_heart_model.pkl')
scaler = joblib.load('scaler.pkl')
@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.post("/predict")
def predict(data:dict):
    input_data=np.array([data["features"]])
    input_scaled=scaler.transform(input_data)
    prediction=model.predict(input_scaled)
    return {"prediction":int(prediction[0])}
                        