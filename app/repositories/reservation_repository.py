from typing import Type

from fastapi import Depends
from fastapi_pagination import Page
from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate

from app.dependencies.database import get_db
from app.models import Reservation, User, Screening


class ReservationRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_reservation(self, screening: Screening, seats: list, current_user: User) -> Reservation:
        db_reservation = Reservation(screening=screening, seats=seats, user=current_user)
        self.db.add(db_reservation)
        self.db.commit()
        self.db.refresh(db_reservation)
        return db_reservation

    def get_reservations(self, user_id: int) -> Page[Reservation]:
        query = self.db.query(Reservation).filter(Reservation.user_id == user_id)
        return paginate(query)

    def get_reservation_by_id(self, reservation_id: int) -> Type[Reservation] | None:
        return self.db.query(Reservation).filter(Reservation.id == reservation_id).first()
