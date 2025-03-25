from fastapi import FastAPI
import joblib
import numpy as np
import os
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Ensure correct paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

scaler_path = os.path.join(BASE_DIR, 'scaler.pkl')
model_path = os.path.join(BASE_DIR, 'xgboost_heart_model.pkl')

try:
    scaler = joblib.load(scaler_path)
except Exception as e:
    print(f"⚠️ Warning: Failed to load scaler.pkl. Error: {e}")
    scaler = None  # Avoid script breaking

try:
    model = joblib.load(model_path)
except Exception as e:
    print(f"⚠️ Warning: Failed to load model.pkl. Error: {e}")
    model = None  # Avoid script breaking




@app.post("/predict")
def predict(data: dict):
    if model is None or scaler is None:
        return {"error": "Model or scaler not loaded"}

    input_data = np.array([data["features"]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    return {"prediction": int(prediction[0])}
