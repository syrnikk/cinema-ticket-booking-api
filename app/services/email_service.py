from fastapi_mail import ConnectionConfig, FastMail, MessageSchema


class EmailService:
    def __init__(self, conf: ConnectionConfig):
        self.fm = FastMail(conf)

    async def send_message(self, subject, recipients, body, subtype):
        message_schema = MessageSchema(
            subject=subject,
            recipients=recipients,
            body=body,
            subtype=subtype
        )
        await self.fm.send_message(message_schema)
