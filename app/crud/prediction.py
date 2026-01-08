from sqlalchemy.orm import Session

from app.db.models import Prediction
from app.schemas.prediction import PredictionCreate


def create_prediction(
    db: Session,
    prediction_in: PredictionCreate,
    predicted_price: float
):
    prediction = Prediction(
        input_data=prediction_in.input_data,
        predicted_price=predicted_price
    )

    db.add(prediction)
    db.commit()
    db.refresh(prediction)

    return prediction

# Handles database operations for predictions
