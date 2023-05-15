from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str = None
    last_name: str = None
    date_of_birth: datetime = None
    email: str = None
    phone: str | None = None
    role: str = None

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str = None
