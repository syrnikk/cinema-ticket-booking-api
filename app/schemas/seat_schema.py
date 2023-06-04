from pydantic import BaseModel


class SeatBase(BaseModel):
    seat_number: int
    row_number: int


class Seat(SeatBase):
    id: int

    class Config:
        orm_mode = True
