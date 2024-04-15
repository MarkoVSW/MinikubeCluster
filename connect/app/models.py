from sqlalchemy import Column, Integer, Float
from pydantic import BaseModel
from .database import Base

class Data(Base):
    __tablename__ = "ml_data"

    id = Column(Integer, primary_key=True, index=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    previous_close = Column(Float)