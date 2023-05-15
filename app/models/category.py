from sqlalchemy import Column, Integer, String

from app.dependencies.database import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
