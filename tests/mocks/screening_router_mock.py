from datetime import datetime
from typing import Optional

from app.models.screening import Screening
from app.models.user import User, Role
from app.schemas.screening_schema import ScreeningUpdate


class MockScreeningService:
    def get_screenings(
        self, screening_date: datetime, title: str, repertoire_id: int, cinema_id: int, upcoming_events: bool
    ) -> list[Screening]:
        screenings = [
            Screening(start_time=datetime(2023, 6, 27, 18, 0), room_number=1, translation="English", image_format="2D", ticket_price=10.0, id=1, repertoire_id=1),
            Screening(start_time=datetime(2023, 6, 28, 19, 30), room_number=2, translation="Polish", image_format="3D", ticket_price=12.0, id=2, repertoire_id=2),
        ]
        return screenings
    
    def get_screening(self, screening_id: int) -> Optional[Screening]:
        screening = Screening(
            start_time=datetime(2023, 6, 27, 18, 0),
            room_number=1,
            translation="English",
            image_format="2D",
            ticket_price=10.0,
            id=screening_id,
            repertoire_id=1
        )
        return screening
    
    def create_screening(self, screening_create):
        screening = Screening(
            start_time=screening_create.start_time,
            room_number=screening_create.room_number,
            translation=screening_create.translation,
            image_format=screening_create.image_format,
            ticket_price=screening_create.ticket_price,
            repertoire_id=screening_create.repertoire_id
        )
        return screening
    
    def update_screening(self, screening_id: int, screening_update: ScreeningUpdate) -> Optional[Screening]:
        screening = self.get_screening(screening_id)
        if screening:
            screening.start_time = screening_update.start_time
            screening.room_number = screening_update.room_number
            screening.translation = screening_update.translation
            screening.image_format = screening_update.image_format
            screening.ticket_price = screening_update.ticket_price
            return screening
        else:
            return None
    
class MockUser:
    role = Role.ADMIN