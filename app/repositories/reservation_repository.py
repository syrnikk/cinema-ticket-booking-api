from fastapi import Depends
from sqlalchemy.orm import Session

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
