from typing import Type

from fastapi import Depends
from fastapi_pagination import Page

from app.models import Movie
from app.repositories.movie_repository import MovieRepository
from app.schemas.movie_schema import MovieCreate, MovieUpdate


class MovieService:
    def __init__(self, movie_repository: MovieRepository = Depends()):
        self.movie_repository = movie_repository

    def get_movie(self, movie_id: int) -> Type[Movie] | None:
        return self.movie_repository.get_movie(movie_id)

    def get_movies(self) -> Page[Movie]:
        return self.movie_repository.get_movies()

    def create_movie(self, movie_create: MovieCreate) -> Movie:
        return self.movie_repository.create_movie(movie_create)

    def update_movie(self, movie_id: int, movie_update: MovieUpdate) -> Type[Movie] | None:
        return self.movie_repository.update_movie(movie_id, movie_update)

    def delete_movie(self, movie_id: int) -> Type[Movie] | None:
        return self.movie_repository.delete_movie(movie_id)
