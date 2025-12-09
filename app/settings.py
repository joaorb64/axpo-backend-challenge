from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Axpo Backend Challenge"
    api_version: str = "0.9"
    app_env: str = "development"
    debug_mode: bool = True
    log_level: str = "DEBUG"
    database_url: str = "postgresql+asyncpg://app:app@db:5432/app"

    def __init__(self, **data):
        super().__init__(**data)
        if self.app_env == "production":
            self.debug_mode = False
            self.log_level = "INFO"


settings = Settings()
