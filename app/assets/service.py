from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import async_session
from app.assets.models import Asset
from sqlalchemy.orm import selectinload
from .schemas import Asset as AssetSchema


async def get_all_assets() -> List[AssetSchema]:
    """Get all assets from the database."""
    async with async_session() as session:
        result = await session.execute(
            select(Asset).options(selectinload(Asset.signals))
        )
        assets = result.scalars().all()

    return [AssetSchema.model_validate(a) for a in assets]
