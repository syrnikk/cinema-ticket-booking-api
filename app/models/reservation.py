from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from app.dependencies.database import Base


class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    screening_id = Column(Integer, ForeignKey('screenings.id'))

    user = relationship('User', back_populates='reservations')
    screening = relationship('Screening', back_populates='reservations')
    seats = relationship('Seat', secondary='reservation_seat_association', back_populates='reservations')
