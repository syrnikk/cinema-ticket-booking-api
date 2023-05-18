from typing import Type

from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page

from app.dependencies.auth import get_current_active_user, has_role
from app.models import User
from app.models.user import Role
from app.schemas.cinema_schema import CinemaCreate, CinemaUpdate, Cinema
from app.services.cinema_service import CinemaService

router = APIRouter(tags=["Cinema"])


@has_role([Role.ADMIN])
@router.get("/cinema", response_model=Page[Cinema])
def get_cinemas(cinema_service: CinemaService = Depends(),
                current_user: User = Depends(get_current_active_user)) -> Page[Cinema]:
    cinemas = cinema_service.get_cinemas()
    return cinemas


@has_role([Role.ADMIN])
@router.get("/cinema/{cinema_id}", response_model=Cinema)
def get_cinema(cinema_id: int, cinema_service: CinemaService = Depends(),
               current_user: User = Depends(get_current_active_user)) -> Type[Cinema]:
    cinema = cinema_service.get_cinema(cinema_id)
    if not cinema:
        raise HTTPException(status_code=404, detail="Cinema not found")
    return cinema


@has_role([Role.ADMIN])
@router.post("/cinema", response_model=Cinema)
def create_cinema(cinema_create: CinemaCreate, cinema_service: CinemaService = Depends(),
                  current_user: User = Depends(get_current_active_user)) -> Cinema:
    cinema = cinema_service.create_cinema(cinema_create)
    return cinema


@has_role([Role.ADMIN])
@router.put("/cinema/{cinema_id}", response_model=Cinema)
def update_cinema(cinema_id: int, cinema_update: CinemaUpdate, cinema_service: CinemaService = Depends(),
                  current_user: User = Depends(get_current_active_user)) -> Type[Cinema]:
    cinema = cinema_service.update_cinema(cinema_id, cinema_update)
    if not cinema:
        raise HTTPException(status_code=404, detail="Cinema not found")
    return cinema


@has_role([Role.ADMIN])
@router.delete("/cinema/{cinema_id}", response_model=Cinema)
def delete_cinema(cinema_id: int, cinema_service: CinemaService = Depends(),
                  current_user: User = Depends(get_current_active_user)) -> Type[Cinema]:
    cinema = cinema_service.delete_cinema(cinema_id)
    if not cinema:
        raise HTTPException(status_code=404, detail="Cinema not found")
    return cinema
