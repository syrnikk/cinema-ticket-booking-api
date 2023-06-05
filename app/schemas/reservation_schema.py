from typing import List

from pydantic import BaseModel

from app.schemas.screening_schema import Screening
from app.schemas.seat_schema import Seat, SeatBase


class ReservationCreate(BaseModel):
    screening_id: int
    seats: List[SeatBase]


class Reservation(BaseModel):
    id: int
    screening: Screening | None
    seats: List[Seat] | None

    class Config:
        orm_mode = True
