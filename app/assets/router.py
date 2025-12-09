"""Assets endpoint (v1)."""
from fastapi import APIRouter, HTTPException
from typing import List
from app.assets import service
from .schemas import Asset
from app.logging.logging_config import logger

router = APIRouter(tags=["assets"])


@router.get("/assets", response_model=List[Asset])
async def get_assets() -> List[Asset]:
    """Get all assets with their signals."""
    try:
        assets = await service.get_all_assets()

        if len(assets) == 0:
            raise HTTPException(status_code=404, detail="No assets found")

        return assets
    except Exception as e:
        logger.error(f"Error fetching assets: {e}")
        raise HTTPException(status_code=500, detail=str(e))
