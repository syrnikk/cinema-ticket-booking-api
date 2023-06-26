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
from tests.mocks.category_router_mock import user, mock_get_current_active_user, mock_get_categories, MockCategoryRepository, MockCategoryService, MockUser

client = TestClient(app)
    
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

    category_service = MockCategoryService()

    category = await update_category(category_id, category_update, category_service, current_user=MockUser())

    assert category is not None
    assert category.id == category_id
    assert category.name == "Updated Category"

@pytest.mark.asyncio
async def test_delete_category():
    category_id = 1
    category_service = MockCategoryService()

    category = await delete_category(category_id, category_service, current_user=MockUser())

    assert category is not None
    assert category.id == category_id
    assert category.name == "Deleted Category"