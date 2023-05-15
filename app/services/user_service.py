from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.utils.auth_utils import get_password_hash, verify_password


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.user_repository.get_user_by_id(user_id)

    def get_user_by_email(self, email: str) -> User | None:
        return self.user_repository.get_user_by_email(email)

    def save(self, user: User) -> User:
        return self.user_repository.save(user)

    def change_password(self, user: User, old_password: str, new_password: str):
        if verify_password(old_password, user.password):
            user.password = get_password_hash(new_password)
            self.user_repository.save(user)
            return True
        return False
