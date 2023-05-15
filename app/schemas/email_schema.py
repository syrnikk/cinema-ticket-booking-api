from pydantic import BaseModel


class EmailSchema(BaseModel):
    email: str
