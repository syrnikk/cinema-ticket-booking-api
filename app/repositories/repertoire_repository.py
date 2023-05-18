from typing import Type

from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.models import Repertoire
from app.schemas.repertoire_schema import RepertoireCreate


class RepertoireRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_repertoire(self, cinema_id: int, movie_id: int):
        return self.db.query(Repertoire).filter(
            Repertoire.cinema_id == cinema_id,
            Repertoire.movie_id == movie_id
        ).first()

    def add_movie_to_repertoire(self, repertoire_create: RepertoireCreate) -> Repertoire:
        repertoire = Repertoire(**repertoire_create.dict())
        self.db.add(repertoire)
        self.db.commit()
        self.db.refresh(repertoire)
        return repertoire

    def remove_movie_from_repertoire(self, cinema_id: int, movie_id: int) -> Type[Repertoire] | None:
        repertoire = self.get_repertoire(cinema_id, movie_id)
        if repertoire:
            self.db.delete(repertoire)
            self.db.commit()
        return repertoire
