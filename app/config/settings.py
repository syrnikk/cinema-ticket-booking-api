from pydantic import BaseSettings


class Settings(BaseSettings):
    # project
    PROJECT_NAME: str
    VERSION: str
    DEBUG: bool
    TESTING: bool
    # database
    DATABASE_URL: str
    # authentication
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    # mail
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_STARTTLS: bool
    MAIL_SSL_TLS: bool
    USE_CREDENTIALS: bool
    VALIDATE_CERTS: bool

    class Config:
        env_file = ".env"


settings = Settings()
