# ...existing code...
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, model_validator, Field, ConfigDict


class MeasurementFilter(BaseModel):
    """Query/filter schema for measurements endpoint."""
    signal_ids: List[str] = Field(..., description="IDs dos sinais")
    start: datetime = Field(..., description="Data/hora inicial (ISO-8601)")
    end: datetime = Field(..., description="Data/hora final (ISO-8601)")

    @model_validator(mode="after")
    def check_date_range(self, values):
        start, end = values.get("start"), values.get("end")
        if start is None or end is None:
            return values
        if start >= end:
            raise ValueError("start must be before end")
        return values


class Measurement(BaseModel):
    """Measurement response model."""
    model_config = ConfigDict(from_attributes=True)
    signal_id: int
    timestamp: datetime
    value: float
    unit: Optional[str] = None


class MeasurementStats(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    signal_id: int
    from_date: str
    to_date: str
    count: int
    mean: Optional[float]
    min: Optional[float]
    max: Optional[float]
    median: Optional[float]
    std_dev: Optional[float]
