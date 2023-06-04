from fastapi import Depends

from app.repositories.seat_repository import SeatRepository


class SeatService:
    def __init__(self, seat_repository: SeatRepository = Depends()):
        self.seat_repository = seat_repository

    def get_booked_seats_by_screening_id(self, screening_id: int) -> list:
        return self.seat_repository.get_booked_seats_by_screening_id(screening_id)
