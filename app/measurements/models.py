from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime


class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, index=True)
    signal_id = Column(Integer, ForeignKey("signal.signal_id"), nullable=True)
    timestamp = Column(DateTime, index=True, nullable=False)
    value = Column(Float, nullable=False)
    unit = Column(String, nullable=True)

    signal = relationship("Signal", back_populates="measurements")
