from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page

from app.dependencies.auth import has_role, get_current_active_user
from app.models.user import Role, User
from app.schemas.screening_schema import ScreeningCreate, ScreeningUpdate, Screening
from app.services.screening_service import ScreeningService

router = APIRouter(tags=["Screening"])


@router.get("/screenings")
def get_screenings(
        screening_date: date = None,
        title: str = None,
        repertoire_id: int = None,
        cinema_id: int = None,
        upcoming_events: bool = True,
        screening_service: ScreeningService = Depends()
) -> Page[Screening]:
    screenings = screening_service.get_screenings(screening_date, title, repertoire_id, cinema_id, upcoming_events)
    return screenings


@router.get("/screenings/{screening_id}", response_model=Screening)
def get_screening(screening_id: int, screening_service: ScreeningService = Depends()):
    screening = screening_service.get_screening(screening_id)
    if not screening:
        raise HTTPException(status_code=404, detail="Screening not found")
    return screening


@has_role([Role.ADMIN])
@router.post("/screenings", response_model=Screening)
def create_screening(screening_create: ScreeningCreate, screening_service: ScreeningService = Depends(),
                     current_user: User = Depends(get_current_active_user)):
    try:
        screening = screening_service.create_screening(screening_create)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Screening time overlaps with another screening.")
    return screening


@has_role([Role.ADMIN])
@router.put("/screenings/{screening_id}", response_model=Screening)
def update_screening(screening_id: int, screening_update: ScreeningUpdate,
                     screening_service: ScreeningService = Depends(),
                     current_user: User = Depends(get_current_active_user)):
    screening = screening_service.update_screening(screening_id, screening_update)
    if not screening:
        raise HTTPException(status_code=404, detail="Screening not found")
    return screening


@has_role([Role.ADMIN])
@router.delete("/screenings/{screening_id}")
def delete_screening(screening_id: int, screening_service: ScreeningService = Depends(),
                     current_user: User = Depends(get_current_active_user)) -> int:
    screening = screening_service.delete_screening(screening_id)
    if not screening:
        raise HTTPException(status_code=404, detail="Screening not found")
    return screening.id
