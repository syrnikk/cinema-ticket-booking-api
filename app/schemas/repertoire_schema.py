
from pydantic import BaseModel

from app.schemas.movie_schema import MovieBase


class RepertoireBase(BaseModel):
    cinema_id: int
    movie_id: int


class RepertoireCreate(RepertoireBase):
    pass


class Repertoire(RepertoireBase):
    id: int

    class Config:
        orm_mode = True


class RepertoireMovie(Repertoire, MovieBase):
    pass
