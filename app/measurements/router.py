from fastapi import APIRouter, HTTPException, Query
from typing import List
from datetime import datetime
from .service import calculate_signal_stats, get_measurements
from .schemas import MeasurementStats, Measurement
from .utils import validate_date_range
from app.logging.logging_config import logger

router = APIRouter(tags=["measurements"])


@router.get("/measurements/stats/{signal_id}", response_model=MeasurementStats)
async def stats(signal_id: int,
                from_date: datetime = Query(..., alias="from"),
                to_date: datetime = Query(..., alias="to")):
    try:
        if not validate_date_range(from_date, to_date):
            raise HTTPException(
                status_code=400,
                detail="'from' date must be earlier than 'to' date"
            )

        stats_data = await calculate_signal_stats(int(signal_id), from_date, to_date)
        return stats_data
    except Exception as e:
        logger.error(f"Error calculating stats for signal {signal_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/measurements")
async def measurements(
    signal_list: List[int] = Query(...,
                                   description="Comma-separated signal IDs"),
    from_date: datetime = Query(..., alias="from"),
    to_date: datetime = Query(..., alias="to")
):
    try:
        if not validate_date_range(from_date, to_date):
            raise HTTPException(
                status_code=400,
                detail="'from' date must be earlier than 'to' date"
            )

        data = await get_measurements(signal_list, from_date, to_date)

        return [
            Measurement(
                signal_id=(m.signal_id),
                timestamp=m.timestamp,
                value=m.value,
                unit=m.unit
            )
            for m in data
        ]
    except Exception as e:
        logger.error(f"Error fetching measurements: {e}")
        raise HTTPException(status_code=500, detail=str(e))
