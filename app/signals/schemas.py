"""Signal model definitions."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class Signal(BaseModel):
    """Signal representation."""
    model_config = ConfigDict(from_attributes=True)
    signal_gid: str
    signal_id: int
    signal_name: str
    asset_id: int
    unit: str
