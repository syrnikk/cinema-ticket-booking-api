from fastapi_mail import ConnectionConfig, FastMail, MessageSchema

from app.config.settings import settings


class EmailService:
    def __init__(self, conf: ConnectionConfig = ConnectionConfig(
        MAIL_USERNAME=settings.MAIL_USERNAME,
        MAIL_PASSWORD=settings.MAIL_PASSWORD,
        MAIL_FROM=settings.MAIL_FROM,
        MAIL_PORT=settings.MAIL_PORT,
        MAIL_SERVER=settings.MAIL_SERVER,
        MAIL_STARTTLS=settings.MAIL_STARTTLS,
        MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
        USE_CREDENTIALS=settings.USE_CREDENTIALS,
        VALIDATE_CERTS=settings.VALIDATE_CERTS
    )):
        self.fm = FastMail(conf)

    async def send_message(self, subject, recipients, body, subtype):
        message_schema = MessageSchema(
            subject=subject,
            recipients=recipients,
            body=body,
            subtype=subtype
        )
        await self.fm.send_message(message_schema)
