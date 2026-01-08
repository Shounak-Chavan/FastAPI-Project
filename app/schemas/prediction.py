from pydantic import BaseModel
from typing import Dict


class PredictionCreate(BaseModel):
    input_data: Dict


class PredictionOut(BaseModel):
    id: int
    predicted_price: float

    class Config:
        from_attributes = True

# Defines request and response data shapes for prediction APIs

