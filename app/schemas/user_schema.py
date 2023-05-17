from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str = None
    last_name: str = None
    date_of_birth: datetime = None
    email: str = None
    phone: str | None = None

    class Config:
        orm_mode = True


class UserCreateRequest(UserBase):
    password: str = None


class UserResponse(UserBase):
    role: str = None
