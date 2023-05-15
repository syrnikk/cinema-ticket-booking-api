from fastapi import Depends
from fastapi_mail import ConnectionConfig

from app.config.settings import settings
from app.dependencies.repositories import get_user_repository
from app.repositories.user_repository import UserRepository
from app.services.email_service import EmailService
from app.services.user_service import UserService


def get_user_service(user_repository: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(user_repository)


def get_email_service():
    conf = ConnectionConfig(
        MAIL_USERNAME=settings.MAIL_USERNAME,
        MAIL_PASSWORD=settings.MAIL_PASSWORD,
        MAIL_FROM=settings.MAIL_FROM,
        MAIL_PORT=settings.MAIL_PORT,
        MAIL_SERVER=settings.MAIL_SERVER,
        MAIL_STARTTLS=settings.MAIL_STARTTLS,
        MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
        USE_CREDENTIALS=settings.USE_CREDENTIALS,
        VALIDATE_CERTS=settings.VALIDATE_CERTS
    )
    return EmailService(conf)
