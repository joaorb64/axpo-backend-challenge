from typing import Optional, List
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.measurements.models import Measurement


class Signal(Base):
    __tablename__ = "signal"

    id = Column(Integer, primary_key=True, autoincrement=True)
    signal_gid = Column(String, index=True, unique=True, nullable=False)
    signal_id = Column(Integer, index=True, unique=True, nullable=False)
    signal_name = Column(String, nullable=False)
    unit = Column(String, nullable=True)

    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=True)

    asset = relationship("Asset", back_populates="signals")
    measurements = relationship(Measurement, back_populates="signal")
