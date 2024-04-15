from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
import json
from fastapi import Depends
import requests
from . import models
from . import schema
from . import crud
from .database import SessionLocal, engine
import os
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.post("/data/", response_model=schema.Data)
def create_data(data: schema.Data, db: Session = Depends(get_db)):
    return crud.create_data(db=db, data=data)

@app.get("/data/", response_model=List[schema.Data])
def read_all_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    datas = crud.get_all_data(db, skip=skip, limit=limit)
    return datas

@app.get("/data/{data_id}", response_model=schema.Data)
def read_data(data_id: int, db: Session = Depends(get_db)):
    db_data = crud.get_data(db, data_id=data_id)
    if db_data is None:
        raise HTTPException(status_code=404, detail="ML data not found")
    return db_data

@app.get("/data/last/", response_model=schema.Data)
def read_last_data(db: Session = Depends(get_db)):
    db_data = crud.get_last_row(db)
    if db_data is None:
        raise HTTPException(status_code=404, detail="ML data not found")
    return db_data

@app.delete("/data/{data_id}", response_model=schema.Data)
def delete_data(data_id: int, db: Session = Depends(get_db)):
    db_data = crud.get_data(db, data_id=data_id)
    if db_data is None:
        raise HTTPException(status_code=404, detail="ML data not found")
    return crud.delete_data(db=db, data_id=data_id)

ip_address = "10.97.168.236"
port = "8006"

@app.post("/model/")
def predict(input_data: schema.PredictionInput):
    host = f"{ip_address}:{port}"
    input = {"open": input_data.open, "high": input_data.high, "low": input_data.low, "previous_close": input_data.previous_close}
    model_api_url= f"http://{host}/predict/"
    response = requests.post(model_api_url, json=input)
    response = json.loads(response.content.decode('utf-8'))
    return response