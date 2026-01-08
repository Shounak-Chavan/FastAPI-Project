from sqlalchemy import Column, Integer, Float, JSON, DateTime
from datetime import datetime, timezone

from app.db.base import Base


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    input_data = Column(JSON, nullable=False)
    predicted_price = Column(Float, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

# Models define how database tables look (columns, types, constraints)
# ORM table structure (not table creation)
