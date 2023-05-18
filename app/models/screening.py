import enum

from sqlalchemy import Integer, ForeignKey, Column, DateTime, Enum, Float
from sqlalchemy.orm import relationship

from app.dependencies.database import Base


class ImageFormat(enum.Enum):
    MOVIE_2D = '2D'
    MOVIE_3D = '3D'


class TranslationType(enum.Enum):
    DUBBING = 'Dubbing'
    SUBTITLES = 'Subtitles'
    VOICE_OVER = 'Voice-over'


class Screening(Base):
    __tablename__ = 'screenings'

    id = Column(Integer, primary_key=True)
    repertoire_id = Column(Integer, ForeignKey('repertoire.id'))
    start_time = Column(DateTime, nullable=False)
    room_number = Column(Integer, nullable=False)
    translation = Column(Enum(TranslationType, name='translation_types'), nullable=False)
    image_format = Column(Enum(ImageFormat, name='image_formats'), nullable=False)
    ticket_price = Column(Float, nullable=False)

    repertoire = relationship('Repertoire', back_populates='screenings')
    reservations = relationship('Reservation', back_populates='screening')
