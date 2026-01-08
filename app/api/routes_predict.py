from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Dict, Any
from app.schemas.prediction import PredictionCreate
from app.core.dependencies import get_api_key, get_current_user
from app.services.model_service import predict_car_price
from app.db.session import get_db
from app.crud.prediction import create_prediction


router = APIRouter()


# Helper: convert NumPy types → Python types
def to_python_types(data: Dict[str, Any]) -> Dict[str, Any]:
    clean = {}
    for k, v in data.items():
        # NumPy scalar → Python scalar
        if hasattr(v, "item"):
            clean[k] = v.item()
        else:
            clean[k] = v
    return clean


# Input schema for prediction
class CareFeatures(BaseModel):
    company: str
    year: int
    owner: str
    fuel: str
    seller_type: str
    transmission: str
    km_driven: float
    mileage_mpg: float
    engine_cc: float
    max_power_bhp: float
    torque_nm: float
    seats: float


@router.post("/predict")
def predict_price(
    car: CareFeatures,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
    _=Depends(get_api_key)
):
    # ML prediction
    prediction = predict_car_price(car.model_dump())

    # Ensure JSON-safe input data
    clean_input = to_python_types(car.model_dump())

    # Save prediction to DB
    create_prediction(
        db=db,
        prediction_in=PredictionCreate(input_data=clean_input),
        predicted_price=float(prediction)
    )

    # API response
    return {
        "predicted_price": f"{prediction:,.2f}"
    }

# Handles prediction API requests and coordinates ML, DB, and auth
