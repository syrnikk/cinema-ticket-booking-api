from typing import Type

from fastapi import Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.models import Movie
from app.schemas.movie_schema import MovieUpdate, MovieCreate


class MovieRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_movie(self, movie_id: int) -> Type[Movie] | None:
        return self.db.query(Movie).filter(Movie.id == movie_id).first()

    def get_movies(self) -> Page[Movie]:
        query = self.db.query(Movie)
        return paginate(query)

    def create_movie(self, movie: MovieCreate) -> Movie:
        db_movie = Movie(**movie.dict())
        self.db.add(db_movie)
        self.db.commit()
        self.db.refresh(db_movie)
        return db_movie

    def update_movie(self, movie_id: int, movie: MovieUpdate) -> Type[Movie] | None:
        db_movie = self.get_movie(movie_id)
        if db_movie:
            for key, value in movie.dict(exclude_unset=True).items():
                setattr(db_movie, key, value)
            self.db.commit()
            self.db.refresh(db_movie)
        return db_movie

    def delete_movie(self, movie_id: int) -> Type[Movie] | None:
        db_movie = self.get_movie(movie_id)
        if db_movie:
            self.db.delete(db_movie)
            self.db.commit()
        return db_movie
