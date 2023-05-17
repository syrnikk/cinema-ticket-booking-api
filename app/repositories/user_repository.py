from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.models.user import User


class UserRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def save(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
