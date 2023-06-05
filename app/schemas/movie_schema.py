from datetime import date

from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    category_id: int
    age_restrictions: int
    description: str
    image: str
    trailer_link: str
    duration_minutes: int
    release_date: date


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    pass


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True
