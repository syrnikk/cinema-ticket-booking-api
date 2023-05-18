from datetime import timedelta

from sqlalchemy import event
from sqlalchemy.exc import IntegrityError

from app.dependencies.database import SessionLocal
from app.models import Movie
from app.models.repertoire import Repertoire
from app.models.screening import Screening

db = SessionLocal()


@event.listens_for(Screening, 'before_insert')
def check_screening_availability(mapper, connection, target):
    existing_screening = db.query(Screening).join(Repertoire).join(Movie).filter(
        Repertoire.cinema_id == target.repertoir.cinema_id,
        Screening.room_number == target.room_number,
        Movie.start_time <= target.start_time + timedelta(minutes=target.movie.duration_minutes),
        Movie.start_time + timedelta(minutes=Movie.duration_minutes) >= target.start_time
    ).first()

    if existing_screening:
        raise IntegrityError("Another movie is already showing in this room at the cinema.")
