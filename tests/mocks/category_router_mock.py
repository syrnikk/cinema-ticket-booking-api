from fastapi_pagination import Page
from app.models.category import Category
from app.models.user import Role, User
from app.utils.auth_utils import get_password_hash


first_name = "John"
last_name = "Doe"
user_email = "test@example.com"
user_password = "password123"
date_of_birth= "1990-01-01"
phone="123456789"
role=Role.USER
user = User(
        first_name=first_name,
        last_name=last_name,
        date_of_birth=date_of_birth,
        email=user_email,
        password=get_password_hash(user_password),
        role=role,
        phone=phone,
        disabled=False
    )

def mock_get_current_active_user(user):
    return user

def mock_get_categories():
    categories = [
        Category(id=1, name="Category 1"),
        Category(id=2, name="Category 2"),
        Category(id=3, name="Category 3"),
    ]
    return Page(results=categories, total=len(categories))

class MockCategoryRepository:
    def get_category(self, category_id):
        if category_id == 1:
            return Category(id=1, name="Category 1")
        return None

class MockCategoryService:
    def create_category(self, category_create):
        return Category(id=1, name="Categoty 1")
    async def update_category(self, category_id, category_update):
        return Category(id=category_id, name=category_update.name)
    async def delete_category(self, category_id):
        return Category(id=category_id, name="Deleted Category")

class MockUser:
    role = Role.ADMIN
