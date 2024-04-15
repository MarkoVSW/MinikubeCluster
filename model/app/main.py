from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

class PredictionInput(BaseModel):
    open: float
    high: float
    low: float
    previous_close: float

@app.get("/")
def home() -> str:
    return "Working."

@app.post("/predict/")
def predict(input_data: PredictionInput):
    loaded_model = joblib.load('app/linear_regression_model.joblib')
    predict_data = pd.DataFrame({
        "open": [input_data.open],
        "high": [input_data.high],
        "low": [input_data.low],
        "previous_close": [input_data.previous_close]
    })
    next_day_price = round(loaded_model.predict(predict_data)[0], 2)
    print(f"The predicted price for the next trading day is: {next_day_price}")
    return {"Predicted price": next_day_price}
