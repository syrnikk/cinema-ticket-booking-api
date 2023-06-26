from fastapi import Depends, status
from fastapi.testclient import TestClient
from fastapi_pagination import Page
import pytest
from app.main import app
from app.models.category import Category
from app.routers.category_router import delete_category, update_category
from app.schemas.category_schema import CategoryUpdate
from app.services.category_service import CategoryService
from app.models.user import User, Role
from app.utils.auth_utils import get_password_hash

client = TestClient(app)

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

class MockUser:
    role = Role.ADMIN

def test_get_categories_with_admin_role(monkeypatch):
    user.role=Role.ADMIN
    
    monkeypatch.setattr(CategoryService, "get_categories", mock_get_categories)
    monkeypatch.setattr("app.dependencies.auth.get_current_active_user", mock_get_current_active_user)

    response = client.get(
        "/category",
        headers={"Authorization": "Bearer my_token"},
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_get_category_with_valid_id():
    category_service = CategoryService(category_repository=MockCategoryRepository())

    category = category_service.get_category(1)

    assert category is not None
    assert category.id == 1
    assert category.name == "Category 1"

def test_get_category_with_invalid_id():
    category_service = CategoryService(category_repository=MockCategoryRepository())

    category = category_service.get_category(2)

    assert category is None

@pytest.mark.asyncio
async def test_update_category():
    category_id = 1
    category_update = CategoryUpdate(name="Updated Category")

    class MockCategoryService:
        async def update_category(self, category_id, category_update):
            return Category(id=category_id, name=category_update.name)

    class MockUser:
        role = Role.ADMIN

    category_service = MockCategoryService()

    category = await update_category(category_id, category_update, category_service, current_user=MockUser())

    assert category is not None
    assert category.id == category_id
    assert category.name == "Updated Category"

@pytest.mark.asyncio
async def test_delete_category():
    category_id = 1

    class MockCategoryService:
        async def delete_category(self, category_id):
            # W tym przykładzie, zakładamy, że zawsze zwracamy usuniętą kategorię
            return Category(id=category_id, name="Deleted Category")

    class MockUser:
        role = Role.ADMIN

    category_service = MockCategoryService()

    category = await delete_category(category_id, category_service, current_user=MockUser())

    assert category is not None
    assert category.id == category_id
    assert category.name == "Deleted Category"