from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    category_id: int
    age_restrictions: int
    description: str
    trailer_link: str
    duration_minutes: int


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    pass


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True
