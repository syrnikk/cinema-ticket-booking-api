from datetime import datetime, timedelta, date
from typing import Optional, Type

from fastapi import Depends
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload

from app.dependencies.database import get_db
from app.models import Repertoire, Movie
from app.models.screening import Screening
from app.schemas.screening_schema import ScreeningCreate, ScreeningUpdate


class ScreeningRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_screenings(self, screening_date: date, title: str, repertoire_id: int, cinema_id: int,
                       upcoming_events: bool):
        query = self.db.query(Screening).join(Repertoire).join(Movie)
        if upcoming_events:
            current_datetime = datetime.now()
            query = query.filter(Screening.start_time >= current_datetime).order_by(Screening.start_time)
        if screening_date:
            query = query.filter(func.date(Screening.start_time) == screening_date)
        if title:
            query = query.filter(Movie.title.ilike(f"%{title}%"))
        if cinema_id:
            query = query.filter(Repertoire.cinema_id == cinema_id)
        if repertoire_id:
            query = query.filter(Repertoire.id == repertoire_id)

        return paginate(query)

    def get_screening(self, screening_id: int) -> Optional[Screening]:
        return self.db.query(Screening).filter(Screening.id == screening_id).first()

    def create_screening(self, screening_create: ScreeningCreate) -> Screening:
        screening = Screening(**screening_create.dict())
        self.db.add(screening)
        self.db.commit()
        self.db.refresh(screening)
        return screening

    def update_screening(self, screening_id: int, screening_update: ScreeningUpdate) -> Optional[Screening]:
        screening = self.get_screening(screening_id)
        if screening:
            for field, value in screening_update.dict(exclude_unset=True).items():
                setattr(screening, field, value)
            self.db.commit()
            self.db.refresh(screening)
        return screening

    def delete_screening(self, screening_id: int) -> Optional[Screening]:
        screening = self.get_screening(screening_id)
        if screening:
            self.db.delete(screening)
            self.db.commit()
        return screening

    def get_existing_screening(self, screening: Screening) -> Type[Screening] | None:
        return self.db.query(Screening).join(Repertoire).join(Movie).filter(
            Screening.room_number == screening.room_number,
            Screening.start_time <= screening.start_time + timedelta(minutes=screening.movie.duration_minutes),
            Screening.start_time + timedelta(minutes=Movie.duration_minutes) >= screening.start_time
        ).first()
