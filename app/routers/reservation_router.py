from fastapi import APIRouter, Depends, HTTPException

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
