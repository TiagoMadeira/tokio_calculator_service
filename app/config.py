import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DEBUG: bool = False
    ENABLE_MONOTORING: str = True
    OTEL_EXPORTER_OTLP_ENDPOINT: str
    OTEL_SERVICE_NAME: str
    class Config:
        env_file = f".env.local"
        
settings = Settings()