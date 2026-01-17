from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    app_name: str = "quality-of-life-analytics"
    environment: str = "local"
    
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    cors_allow_origins: List[str] = ["http://localhost:5173"]
    
    admin_api_key: str = "admin"

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
