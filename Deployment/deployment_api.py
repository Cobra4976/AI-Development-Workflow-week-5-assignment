from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(title="Patient Readmission Predictor")

model = joblib.load("readmission_model.pkl")

@app.get("/")
def home():
    return {"message": "Readmission Prediction API is live!"}

@app.post("/predict/")
def predict(data: dict):
    df = pd.DataFrame([data])
    pred = model.predict(df)[0]
    return {"readmission_risk": int(pred)}
