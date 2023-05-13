from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate
from app.utils.auth_utils import get_password_hash


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.user_repository.get_user_by_id(user_id)

    def get_user_by_email(self, email: str) -> User | None:
        return self.user_repository.get_user_by_email(email)

    def create_user(self, user_data: UserCreate) -> User:
        user = User(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            password=get_password_hash(user_data.password),
            phone=user_data.phone
        )
        return self.user_repository.create_user(user)
