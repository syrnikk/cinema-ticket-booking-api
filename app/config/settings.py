import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Cinema Ticket Booking API"
    VERSION: str = "0.0.1"
    DEBUG: bool = False
    TESTING: bool = False
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")

    class Config:
        env_file = ".env"


settings = Settings()
