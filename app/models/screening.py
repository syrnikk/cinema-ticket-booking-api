from sqlalchemy import Integer, ForeignKey, Column, DateTime, Enum, Float
from sqlalchemy.orm import relationship

from app.dependencies.database import Base


class Screening(Base):
    __tablename__ = 'screenings'

    id = Column(Integer, primary_key=True)
    repertoir_id = Column(Integer, ForeignKey('repertoir.id'))
    start_time = Column(DateTime, nullable=False)
    room_number = Column(Integer, nullable=False)
    translation = Column(Enum('Dubbing', 'Subtitles', 'Voice-over', name='translation_types'), nullable=False)
    image_format = Column(Enum('2D', '3D', name='image_formats'), nullable=False)
    ticket_price = Column(Float, nullable=False)

    repertoir = relationship('Repertoir', back_populates='screenings')
    reservations = relationship('Reservation', back_populates='screening')
