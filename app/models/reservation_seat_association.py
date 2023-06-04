from sqlalchemy import Column, Integer, ForeignKey

from app.dependencies.database import Base


class ReservationSeatAssociation(Base):
    __tablename__ = 'reservation_seat_association'

    reservation_id = Column(Integer, ForeignKey('reservations.id'), primary_key=True)
    seat_id = Column(Integer, ForeignKey('seats.id'), primary_key=True)
