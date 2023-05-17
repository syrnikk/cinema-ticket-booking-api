from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from sqlalchemy.orm import relationship

from app.dependencies.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    reset_token = Column(String)
    phone = Column(String)
    role = Column(Enum('admin', 'user', name='user_roles'), nullable=False)
    disabled = Column(Boolean, default=False)

    reservations = relationship('Reservation', back_populates='user')
