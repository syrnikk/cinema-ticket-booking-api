from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.dependencies.database import Base


class Cinema(Base):
    __tablename__ = 'cinemas'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)

    repertoir = relationship('Repertoir', back_populates='cinema')
