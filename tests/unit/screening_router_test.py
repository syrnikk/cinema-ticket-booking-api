from fastapi import Depends, status
from fastapi.testclient import TestClient
from fastapi_pagination import Page, Params
import pytest
from app.main import app
from datetime import date, datetime
from typing import Optional
from app.models.screening import Screening
from app.routers.screening_router import create_screening, get_screening, get_screenings, update_screening
from app.schemas.screening_schema import ScreeningCreate, ScreeningUpdate
from tests.mocks.screening_router_mock import MockScreeningService, MockUser

client = TestClient(app)

@pytest.mark.asyncio
async def test_get_screenings():
    screening_service = MockScreeningService()
    screening_date = datetime(2023, 6, 27, 0, 0)
    title = "Movie Title"
    repertoire_id = 1
    cinema_id = 1
    upcoming_events = True

    result = get_screenings(
        screening_date, title, repertoire_id, cinema_id, upcoming_events, screening_service
    )

    assert result is not None
    assert isinstance(result, list)
    assert all(isinstance(screening, Screening) for screening in result)

@pytest.mark.asyncio
async def test_get_screening():
    screening_service = MockScreeningService()
    screening_id = 1

    result = get_screening(screening_id, screening_service)

    assert result is not None
    assert isinstance(result, Screening)
    assert result.id == screening_id