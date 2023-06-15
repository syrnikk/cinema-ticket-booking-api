from sqlalchemy import Integer, Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.dependencies.database import Base


class Repertoire(Base):
    __tablename__ = 'repertoire'

    id = Column(Integer, primary_key=True)
    cinema_id = Column(Integer, ForeignKey('cinemas.id'), nullable=False)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)

    cinema = relationship('Cinema', back_populates='repertoire')
    movie = relationship('Movie', back_populates='repertoire')
    screenings = relationship('Screening', back_populates='repertoire')

    __table_args__ = (
        UniqueConstraint('cinema_id', 'movie_id', name="uq_cinema_movie"),
    )
