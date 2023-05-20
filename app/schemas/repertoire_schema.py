
from pydantic import BaseModel

from app.schemas.movie_schema import MovieBase, Movie


class RepertoireBase(BaseModel):
    cinema_id: int


class RepertoireCreate(RepertoireBase):
    pass


class Repertoire(RepertoireBase):
    id: int
    movie: Movie | None

    class Config:
        orm_mode = True


class RepertoireMovie(Repertoire, MovieBase):
    pass
