from datetime import date
from typing import Optional

from fastapi import Depends
from fastapi_pagination import Page

from app.models.screening import Screening
from app.repositories.screening_repository import ScreeningRepository
from app.schemas.screening_schema import ScreeningCreate, ScreeningUpdate


class ScreeningService:
    def __init__(self, screening_repository: ScreeningRepository = Depends()):
        self.screening_repository = screening_repository

    def get_screenings(self, screening_date: date, title: str, repertoire_id: int, cinema_id: int, upcoming_events: bool) -> Page[Screening]:
        return self.screening_repository.get_screenings(screening_date, title, repertoire_id, cinema_id, upcoming_events)

    def get_screening(self, screening_id: int) -> Optional[Screening]:
        return self.screening_repository.get_screening(screening_id)

    def create_screening(self, screening_create: ScreeningCreate) -> Screening:
        return self.screening_repository.create_screening(screening_create)

    def update_screening(self, screening_id: int, screening_update: ScreeningUpdate) -> Optional[Screening]:
        return self.screening_repository.update_screening(screening_id, screening_update)

    def delete_screening(self, screening_id: int) -> Optional[Screening]:
        return self.screening_repository.delete_screening(screening_id)
