from typing import List

from pydantic import BaseModel

from app.schemas.screening_schema import Screening
from app.schemas.seat_schema import Seat, SeatBase
from app.schemas.user_schema import User


class ReservationCreate(BaseModel):
    screening_id: int
    seats: List[SeatBase]


class Reservation(BaseModel):
    id: int
    user: User
    screening: Screening
    seats: List[Seat]

    class Config:
        orm_mode = True
