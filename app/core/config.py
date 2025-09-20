from __future__ import annotations
from pydantic_settings import BaseSettings
from pydantic import AnyUrl

class Settings(BaseSettings):
    app_name: str = "fastapi-user-service"
    env: str = "local"

    database_url: AnyUrl

    jwt_secret: str
    jwt_alg: str = "HS256"
    jwt_expires_min: int = 60

    email_api_base: str
    email_send_path: str
    email_api_token: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

settings = Settings()  # singleton
