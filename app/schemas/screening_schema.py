from datetime import datetime

from pydantic import BaseModel

from app.schemas.repertoire_schema import Repertoire


class ScreeningBase(BaseModel):
    start_time: datetime
    room_number: int
    translation: str
    image_format: str
    ticket_price: float


class ScreeningCreate(ScreeningBase):
    repertoire_id: int


class ScreeningUpdate(ScreeningBase):
    pass


class Screening(ScreeningBase):
    id: int
    repertoire: Repertoire | None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
