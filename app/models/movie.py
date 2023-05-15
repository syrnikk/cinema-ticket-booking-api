from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.dependencies.database import Base


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    age_restrictions = Column(Integer)
    description = Column(String(255))
    trailer_link = Column(String(255))
    duration_minutes = Column(Integer)

    category = relationship('Category', backref='movies')
    repertoir = relationship('Repertoir', back_populates='movie')
