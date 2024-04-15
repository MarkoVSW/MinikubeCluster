from pydantic import BaseModel

class Data(BaseModel):
    id: int
    open: float
    high: float
    low: float
    previous_close: float
    
    class Config:
        from_attributes = True

class PredictionInput(BaseModel):
    open: float
    high: float
    low: float
    previous_close: float