from sqlalchemy import Integer, Column, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship

from app.dependencies.database import Base


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    age_restrictions = Column(Integer)
    description = Column(String(255), nullable=False)
    image = Column(Text, nullable=False)
    trailer_link = Column(String(255), nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    release_date = Column(Date, nullable=False)

    category = relationship('Category', backref='movies')
    repertoire = relationship('Repertoire', back_populates='movie')
