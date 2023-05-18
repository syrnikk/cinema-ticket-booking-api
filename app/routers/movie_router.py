from typing import Type

from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page

from app.dependencies.auth import get_current_active_user, has_role
from app.models import User
from app.models.user import Role
from app.schemas.movie_schema import MovieCreate, MovieUpdate, Movie
from app.services.movie_service import MovieService

router = APIRouter(tags=["Movie"])


@has_role([Role.ADMIN])
@router.get("/movie", response_model=Page[Movie])
def get_movies(movie_service: MovieService = Depends(),
               current_user: User = Depends(get_current_active_user)) -> Page[Movie]:
    movies = movie_service.get_movies()
    return movies


@has_role([Role.ADMIN])
@router.get("/movie/{movie_id}", response_model=Movie)
def get_movie(movie_id: int, movie_service: MovieService = Depends(),
              current_user: User = Depends(get_current_active_user)) -> Type[Movie]:
    movie = movie_service.get_movie(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@has_role([Role.ADMIN])
@router.post("/movie", response_model=Movie)
def create_movie(movie_create: MovieCreate, movie_service: MovieService = Depends(),
                 current_user: User = Depends(get_current_active_user)) -> Movie:
    movie = movie_service.create_movie(movie_create)
    return movie


@has_role([Role.ADMIN])
@router.put("/movie/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, movie_update: MovieUpdate, movie_service: MovieService = Depends(),
                 current_user: User = Depends(get_current_active_user)) -> Type[Movie]:
    movie = movie_service.update_movie(movie_id, movie_update)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@has_role([Role.ADMIN])
@router.delete("/movie/{movie_id}", response_model=Movie)
def delete_movie(movie_id: int, movie_service: MovieService = Depends(),
                 current_user: User = Depends(get_current_active_user)) -> Type[Movie]:
    movie = movie_service.delete_movie(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie
