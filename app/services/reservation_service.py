from fastapi import Depends

from app.models import Reservation, User
from app.repositories.reservation_repository import ReservationRepository
from app.repositories.screening_repository import ScreeningRepository
from app.repositories.seat_repository import SeatRepository
from app.schemas.reservation_schema import ReservationCreate


class ReservationService:
    def __init__(self, reservation_repository: ReservationRepository = Depends(),
                 seat_repository: SeatRepository = Depends(), screening_repository: ScreeningRepository = Depends()):
        self.reservation_repository = reservation_repository
        self.seat_repository = seat_repository
        self.screening_repository = screening_repository

    def create_reservation(self, reservation: ReservationCreate, current_user: User) -> Reservation:
        screening = self.screening_repository.get_screening(reservation.screening_id)
        if screening is None:
            raise ValueError(f"Screening with id: {reservation.screening_id} does not exist.")
        db_seats = []
        for seat in reservation.seats:
            db_seat = self.seat_repository.get_seat_by_row_and_seat_number(seat.row_number, seat.seat_number)
            if self.seat_repository.is_seat_booked(reservation.screening_id, db_seat.id):
                raise ValueError(
                    f"Seat {seat.seat_number} in row {seat.row_number} is already booked for the specified screening.")
            db_seats.append(db_seat)
        return self.reservation_repository.create_reservation(screening, db_seats, current_user)
