from fastapi import Depends, status
from fastapi.testclient import TestClient
from fastapi_pagination import Page
import pytest
from app.main import app
from app.models.cinema import Cinema
from app.routers.cinema_router import create_cinema, delete_cinema, get_cinema, get_cinemas, update_cinema
from app.schemas.cinema_schema import CinemaCreate, CinemaUpdate
from tests.mocks.cinema_router_mock import MockCinemaService, MockUser

client = TestClient(app)

@pytest.mark.asyncio
async def test_get_cinemas():
    cinema_service = MockCinemaService()

    result = await get_cinemas(cinema_service, current_user=MockUser())

    assert result is not None
    assert isinstance(result, Page)
    assert len(result.items) == 3
    assert result.total == 3
    assert result.page == 1
    assert result.size == 10
    assert all(isinstance(cinema, Cinema) for cinema in result.items)

@pytest.mark.asyncio
async def test_get_cinema():
    cinema_service = MockCinemaService()

    result = await get_cinema(cinema_id=1, cinema_service=cinema_service, current_user=MockUser())

    assert result is not None
    assert isinstance(result, Cinema)
    assert result.id == 1
    assert result.name == "Cinema 1"

@pytest.mark.asyncio
async def test_create_cinema():
    cinema_service = MockCinemaService()

    cinema_create = CinemaCreate(name="New Cinema", location="Location")
    result = await create_cinema(cinema_create=cinema_create, cinema_service=cinema_service, current_user=MockUser())

    assert result is not None
    assert isinstance(result, Cinema)
    assert result.id == 1
    assert result.name == "New Cinema"
    assert result.location == "Location"

@pytest.mark.asyncio
async def test_update_cinema():
    cinema_service = MockCinemaService()

    cinema_update = CinemaUpdate(name="Updated Cinema", location="New Location")
    result = await update_cinema(cinema_id=1, cinema_update=cinema_update, cinema_service=cinema_service, current_user=MockUser())

    assert result is not None
    assert isinstance(result, Cinema)
    assert result.id == 1
    assert result.name == "Updated Cinema"
    assert result.location == "New Location"


@pytest.mark.asyncio
async def test_delete_cinema():
    cinema_service = MockCinemaService()

    result = await delete_cinema(cinema_id=1, cinema_service=cinema_service, current_user=MockUser())

    assert result is not None
    assert isinstance(result, Cinema)
    assert result.id == 1
    assert result.name == "Deleted Cinema"
    assert result.location == "Deleted Location"