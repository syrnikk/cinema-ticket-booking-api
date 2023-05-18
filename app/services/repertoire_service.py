from typing import Type

from fastapi import Depends

from app.models import Repertoire
from app.repositories.repertoire_repository import RepertoireRepository
from app.schemas.repertoire_schema import RepertoireCreate


class RepertoireService:
    def __init__(self, repertoire_repository: RepertoireRepository = Depends()):
        self.repertoire_repository = repertoire_repository

    def get_repertoire(self, cinema_id: int, movie_id: int):
        return self.repertoire_repository.get_repertoire(cinema_id, movie_id)

    def add_movie_to_repertoire(self, repertoire_create: RepertoireCreate) -> Repertoire:
        return self.repertoire_repository.add_movie_to_repertoire(repertoire_create)

    def remove_movie_from_repertoire(self, cinema_id: int, movie_id: int) -> Type[Repertoire] | None:
        return self.repertoire_repository.remove_movie_from_repertoire(cinema_id, movie_id)
