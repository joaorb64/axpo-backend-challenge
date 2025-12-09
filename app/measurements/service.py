import statistics
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from app.measurements.models import Measurement
from app.db.database import async_session
from .schemas import MeasurementStats


async def get_measurements(signal_ids: List[int], from_dt: datetime, to_dt: datetime) -> List[Measurement]:
    async with async_session() as session:
        result = await session.execute(
            select(Measurement)
            .where(
                Measurement.signal_id.in_(signal_ids),
                Measurement.timestamp >= from_dt,
                Measurement.timestamp <= to_dt
            )
        )
        return result.scalars().all()


async def calculate_signal_stats(signal_id: int, from_dt: datetime, to_dt: datetime) -> MeasurementStats:
    """Calcula estatísticas para um sinal em um intervalo de datas."""
    measurements = await get_measurements([signal_id], from_dt, to_dt)
    values = [m.value for m in measurements]

    if not values:
        return MeasurementStats(
            signal_id=signal_id,
            from_date=from_dt.isoformat(),
            to_date=to_dt.isoformat(),
            count=0,
            mean=None,
            min=None,
            max=None,
            median=None,
            std_dev=None
        )

    return MeasurementStats(
        signal_id=signal_id,
        from_date=from_dt.isoformat(),
        to_date=to_dt.isoformat(),
        count=len(values),
        mean=round(statistics.mean(values), 2),
        min=round(min(values), 2),
        max=round(max(values), 2),
        median=round(statistics.median(values), 2),
        std_dev=round(statistics.stdev(values), 2) if len(values) > 1 else 0.0
    )
