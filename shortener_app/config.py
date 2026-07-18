# Loads application configuration from environment variables.

from pydantic_settings import BaseSettings, SettingsConfigDict

from functools import lru_cache

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


# settings = Settings()

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()