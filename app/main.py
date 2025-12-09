"""Application factory and configuration."""
from fastapi import FastAPI
from app.settings import settings
from app.health import router as health_router
from app.assets import router as asset_router
from app.measurements import router as measurement_router
from app.db.database import init_db
# from app.signals import router as signal_router
import uvicorn


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title=settings.app_name,
        version=settings.api_version
    )

    # Register routers
    app.include_router(health_router.router)
    app.include_router(asset_router.router)
    app.include_router(measurement_router.router)

    return app


app = create_app()


@app.on_event("startup")
async def on_startup():
    await init_db()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
