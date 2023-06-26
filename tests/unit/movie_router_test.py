import pytest
from fastapi import HTTPException, status
from fastapi.testclient import TestClient
from app.main import app
from app.models.movie import Movie
from app.routers.movie_router import create_movie, delete_movie, get_movie, get_movies, update_movie
from fastapi_pagination import Page
from app.schemas.movie_schema import MovieCreate
from tests.mocks.movie_router_mock import MockMovieService, MockUser, movie_create, movie_update

client = TestClient(app)

@pytest.mark.asyncio
async def test_get_movies():
    movie_service = MockMovieService()

    result = await get_movies(movie_service=movie_service, current_user=MockUser())

    assert result is not None
    assert isinstance(result, Page)
    assert len(result.items) == 3
    assert result.items[0].id == 1
    assert result.items[0].title == "Movie 1"
    assert result.items[1].id == 2
    assert result.items[1].title == "Movie 2"
    assert result.items[2].id == 3
    assert result.items[2].title == "Movie 3"
    assert result.total == 3

@pytest.mark.asyncio
async def test_get_movie():
    movie_service = MockMovieService()

    result = await get_movie(movie_id=1, movie_service=movie_service, current_user=MockUser())

    assert result is not None
    assert isinstance(result, Movie)
    assert result.id == 1
    assert result.title == "Movie 1"

@pytest.mark.asyncio
async def test_create_movie():
    movie_service = MockMovieService()

    result = await create_movie(movie_create=movie_create, movie_service=movie_service, current_user=MockUser())

    assert result is not None
    assert isinstance(result, Movie)
    assert result.id == 1
    assert result.title == "New Movie"

@pytest.mark.asyncio
async def test_update_movie():
    movie_service = MockMovieService()

    movie_id = 1
    result = await update_movie(movie_id=movie_id, movie_update=movie_update, movie_service=movie_service, current_user=MockUser())

    assert result is not None
    assert isinstance(result, Movie)
    assert result.id == 1
    assert result.title == "Updated Movie"

@pytest.mark.asyncio
async def test_delete_movie():
    movie_service = MockMovieService()

    movie_id = 1
    result = await delete_movie(movie_id=movie_id, movie_service=movie_service, current_user=MockUser())

    assert result is not None
    assert isinstance(result, Movie)
    assert result.id == 1
    assert result.title == "Deleted Movie"