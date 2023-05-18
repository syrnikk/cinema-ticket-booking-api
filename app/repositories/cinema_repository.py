from typing import Type

from fastapi import Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.models import Cinema
from app.schemas.cinema_schema import CinemaCreate, CinemaUpdate


class CinemaRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_cinema(self, cinema_id: int) -> Type[Cinema] | None:
        return self.db.query(Cinema).filter(Cinema.id == cinema_id).first()

    def get_cinemas(self) -> Page[Cinema]:
        query = self.db.query(Cinema)
        return paginate(query)

    def create_cinema(self, cinema_create: CinemaCreate) -> Cinema:
        cinema = Cinema(**cinema_create.dict())
        self.db.add(cinema)
        self.db.commit()
        self.db.refresh(cinema)
        return cinema

    def update_cinema(self, cinema_id: int, cinema_update: CinemaUpdate) -> Type[Cinema] | None:
        cinema = self.get_cinema(cinema_id)
        if cinema:
            for key, value in cinema_update.dict().items():
                setattr(cinema, key, value)
            self.db.commit()
            self.db.refresh(cinema)
        return cinema

    def delete_cinema(self, cinema_id: int) -> Type[Cinema] | None:
        cinema = self.get_cinema(cinema_id)
        if cinema:
            self.db.delete(cinema)
            self.db.commit()
        return cinema
