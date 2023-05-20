from fastapi import HTTPException, Depends

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserUpdate
from app.utils.auth_utils import get_password_hash, verify_password


class UserService:
    def __init__(self, user_repository: UserRepository = Depends()):
        self.user_repository = user_repository

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.user_repository.get_user_by_id(user_id)

    def get_user_by_email(self, email: str) -> User | None:
        return self.user_repository.get_user_by_email(email)

    def save(self, user: User) -> User:
        return self.user_repository.save(user)

    def update_user(self, user_id: int, user_update: UserUpdate) -> User:
        user = self.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        for field, value in user_update.dict(exclude_unset=True).items():
            setattr(user, field, value)
        self.user_repository.update_user(user)
        return user

    def delete_user(self, user: User):
        self.user_repository.delete_user(user)

    def change_password(self, user: User, old_password: str, new_password: str):
        if verify_password(old_password, user.password):
            user.password = get_password_hash(new_password)
            self.user_repository.save(user)
            return True
        return False

    def reset_password(self, user: User, reset_token: str, new_password: str):
        if reset_token != user.reset_token:
            raise HTTPException(status_code=400, detail="Invalid token")
        user.password = get_password_hash(new_password)
        user.reset_token = None
        self.user_repository.save(user)
