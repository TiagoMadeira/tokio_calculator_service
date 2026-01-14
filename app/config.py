import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV: str
    DEBUG: bool
    OTEL_EXPORTER_OTLP_ENDPOINT: str
    OTEL_SERVICE_NAME: str
    class Config:
        env_file = f".env.{os.getenv('ENV', 'development')}"
        
settings = Settings()