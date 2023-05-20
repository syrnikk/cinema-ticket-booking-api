from typing import Type

from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, paginate

from app.dependencies.auth import has_role, get_current_active_user

from app.models.user import Role, User
from app.schemas.repertoire_schema import RepertoireCreate, Repertoire, RepertoireMovie
from app.services.cinema_service import CinemaService
from app.services.repertoire_service import RepertoireService

router = APIRouter(tags=["Repertoire"])


@router.get("/repertoire/{cinema_id}/movies", response_model=Page[RepertoireMovie], response_model_exclude_unset=True)
def get_movies_by_cinema_id(cinema_id: int, cinema_service: CinemaService = Depends()):
    cinema = cinema_service.get_cinema(cinema_id)
    if not cinema:
        return []

    repertoire_movie_list = [RepertoireMovie(
        id=repertoire.id,
        cinema_id=repertoire.cinema_id,
        movie_id=repertoire.movie_id,
        title=repertoire.movie.title,
        category_id=repertoire.movie.category_id,
        age_restrictions=repertoire.movie.age_restrictions,
        description=repertoire.movie.description,
        trailer_link=repertoire.movie.trailer_link,
        duration_minutes=repertoire.movie.duration_minutes,
        release_date=repertoire.movie.release_date
    ) for repertoire in cinema.repertoire]

    return paginate(repertoire_movie_list)


@has_role([Role.ADMIN])
@router.post("/repertoire", response_model=Repertoire)
def add_movie_to_repertoire(repertoire_create: RepertoireCreate,
                            repertoire_service: RepertoireService = Depends(),
                            current_user: User = Depends(get_current_active_user)) -> Repertoire:
    repertoire = repertoire_service.get_repertoire(repertoire_create.cinema_id, repertoire_create.movie_id)
    if repertoire:
        raise HTTPException(status_code=404, detail="Movie already exists in cinema repertoire")
    return repertoire_service.add_movie_to_repertoire(repertoire_create)


@has_role([Role.ADMIN])
@router.delete("/repertoire/{cinema_id}/{movie_id}")
def remove_movie_from_repertoire(cinema_id: int, movie_id: int,
                                 repertoire_service: RepertoireService = Depends(),
                                 current_user: User = Depends(get_current_active_user)) -> int:
    repertoire = repertoire_service.remove_movie_from_repertoire(cinema_id, movie_id)
    if not repertoire:
        raise HTTPException(status_code=404, detail="Repertoire not found")
    return repertoire.id
