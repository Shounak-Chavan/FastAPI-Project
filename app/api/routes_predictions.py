from fastapi import APIRouter ,Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.core.dependencies import get_current_user , get_api_key
from app.crud.prediction import get_predictions
from app.schemas.prediction import PredictionOut

router = APIRouter()

@router.get("/predictions",response_model=List[PredictionOut])
def read_predictions(
    db:Session = Depends(get_db),
    user = Depends(get_current_user),
    _ = Depends(get_api_key)
):
    return get_predictions(db=db)