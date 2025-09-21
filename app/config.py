# app/config.py
from typing import List
from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = Field(..., description="App name")
    API_PREFIX: str = Field(..., description="API prefix")
    SECRET_KEY: str = Field(..., description="JWT secret")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(..., description="Token lifetime in minutes")
    SQLITE_URL: str = Field(..., description="Database URL")
    CORS_ALLOW_ORIGINS: List[str] = Field(..., description="CORS origins")

    class Config:
        env_file = ".env"

settings = Settings()
