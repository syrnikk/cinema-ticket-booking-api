from sqlalchemy import Integer, Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.dependencies.database import Base


class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    screening_id = Column(Integer, ForeignKey('screenings.id'))
    seat_number = Column(Integer, nullable=False)
    row_number = Column(Integer, nullable=False)

    user = relationship('User', back_populates='reservations')
    screening = relationship('Screening', back_populates='reservations')

    __table_args__ = (
        UniqueConstraint('screening_id', 'seat_number', 'row_number', name='uq_screening_seat_row'),
    )
