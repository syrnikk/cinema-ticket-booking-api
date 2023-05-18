from typing import Type

from fastapi import Depends
from fastapi_pagination import Page
from app.models import Cinema
from app.repositories.cinema_repository import CinemaRepository
from app.schemas.cinema_schema import CinemaCreate, CinemaUpdate


class CinemaService:
    def __init__(self, cinema_repository: CinemaRepository = Depends()):
        self.cinema_repository = cinema_repository

    def get_cinema(self, cinema_id: int) -> Type[Cinema] | None:
        return self.cinema_repository.get_cinema(cinema_id)

    def get_cinemas(self) -> Page[Cinema]:
        return self.cinema_repository.get_cinemas()

    def create_cinema(self, cinema_create: CinemaCreate) -> Cinema:
        return self.cinema_repository.create_cinema(cinema_create)

    def update_cinema(self, cinema_id: int, cinema_update: CinemaUpdate) -> Type[Cinema] | None:
        return self.cinema_repository.update_cinema(cinema_id, cinema_update)

    def delete_cinema(self, cinema_id: int) -> Type[Cinema] | None:
        return self.cinema_repository.delete_cinema(cinema_id)
