from pydantic import BaseModel


class CinemaBase(BaseModel):
    name: str
    location: str


class CinemaCreate(CinemaBase):
    pass


class CinemaUpdate(CinemaBase):
    pass


class Cinema(CinemaBase):
    id: int

    class Config:
        orm_mode = True