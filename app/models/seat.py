from sqlalchemy import Column, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship

from app.dependencies.database import Base


class Seat(Base):
    __tablename__ = 'seats'

    id = Column(Integer, primary_key=True)
    seat_number = Column(Integer, nullable=False)
    row_number = Column(Integer, nullable=False)

    reservations = relationship('Reservation', secondary='reservation_seat_association', back_populates='seats')
