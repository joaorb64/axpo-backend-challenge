from typing import List, Dict
from pydantic import BaseModel, ConfigDict
from app.signals.schemas import Signal


class Asset(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    asset_id: str
    signals: List[Signal]
