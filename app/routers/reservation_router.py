from typing import Type

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi_pagination import Page

from app.dependencies.auth import get_current_active_user
from app.models import User
from app.schemas.reservation_schema import ReservationCreate, Reservation
from app.services.reservation_service import ReservationService

router = APIRouter(tags=["Reservation"])


@router.post("/reservations", response_model=Reservation, status_code=201)
def create_reservation(reservation_create: ReservationCreate, reservation_service: ReservationService = Depends(),
                       current_user: User = Depends(get_current_active_user)):
    try:
        reservation = reservation_service.create_reservation(reservation_create, current_user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return reservation


@router.get("/reservations")
def get_reservations(user_id: int = Query(None), reservation_service: ReservationService = Depends(),
                     current_user: User = Depends(get_current_active_user)) -> Page[Reservation]:
    if user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Cannot list other user reservations")
    reservations = reservation_service.get_reservations(user_id)
    return reservations


@router.get("/reservations/{reservation_id}", response_model=Reservation)
def get_reservations(reservation_id: int, reservation_service: ReservationService = Depends(),
                     current_user: User = Depends(get_current_active_user)) -> Type[Reservation] | None:
    reservation = reservation_service.get_reservation_by_id(reservation_id)
    if reservation.user.id != current_user.id:
        raise HTTPException(status_code=403, detail="Cannot list other user reservations")
    return reservation
