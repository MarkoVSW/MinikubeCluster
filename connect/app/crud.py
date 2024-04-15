from sqlalchemy.orm import Session
from sqlalchemy import desc
from . import models
from . import schema

def get_data(db: Session, data_id: int):
    return db.query(models.Data).filter(models.Data.id == data_id).first()

def get_all_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Data).offset(skip).limit(limit).all()

def get_last_row(db:Session):
    return db.query(models.Data).order_by(desc(models.Data.id)).first()

def create_data(db: Session, data: schema.Data):
    db_data = models.Data(id=data.id, open=data.open, high=data.high, low=data.low, previous_close=data.previous_close)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_data(db: Session, data_id: int):
    db_data = db.query(models.Data).filter(models.Data.id == data_id).first()
    if db_data:
        db.delete(db_data)
        db.commit()
    return db_data