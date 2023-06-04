from typing import Type

from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.models import Reservation, ReservationSeatAssociation
from app.models.seat import Seat


class SeatRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_booked_seats_by_screening_id(self, screening_id: int) -> list:
        booked_seats = self.db.query(Seat).join(Reservation.seats).filter(
            Reservation.screening_id == screening_id).all()
        return booked_seats

    def is_seat_booked(self, screening_id: int, seat_id: int) -> bool:
        return (
                self.db.query(ReservationSeatAssociation)
                .join(Reservation)
                .filter(
                    Reservation.screening_id == screening_id,
                    ReservationSeatAssociation.seat_id == seat_id
                )
                .first() is not None
        )

    def get_seat_by_row_and_seat_number(self, row_number: int, seat_number: int) -> Type[Seat] | None:
        return self.db.query(Seat).filter(Seat.row_number == row_number, Seat.seat_number == seat_number).first()
