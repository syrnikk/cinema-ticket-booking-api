from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from app.dependencies.database import Base


class Repertoir(Base):
    __tablename__ = 'repertoir'

    id = Column(Integer, primary_key=True)
    cinema_id = Column(Integer, ForeignKey('cinemas.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))

    cinema = relationship('Cinema', back_populates='repertoir')
    movie = relationship('Movie', back_populates='repertoir')
    screenings = relationship('Screening', back_populates='repertoir')