from typing import Type

from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page

from app.dependencies.auth import get_current_active_user, has_role
from app.models import User
from app.models.user import Role
from app.schemas.category_schema import CategoryCreate, CategoryUpdate, Category
from app.services.category_service import CategoryService

router = APIRouter(tags=["Category"])


@has_role([Role.ADMIN])
@router.get("/category", response_model=Page[Category])
def get_categories(category_service: CategoryService = Depends(),
                   current_user: User = Depends(get_current_active_user)) -> Page[Category]:
    categories = category_service.get_categories()
    return categories


@has_role([Role.ADMIN])
@router.get("/category/{category_id}", response_model=Category)
def get_category(category_id: int, category_service: CategoryService = Depends(),
                 current_user: User = Depends(get_current_active_user)) -> Type[Category]:
    category = category_service.get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@has_role([Role.ADMIN])
@router.post("/category", response_model=Category)
def create_category(category_create: CategoryCreate, category_service: CategoryService = Depends(),
                    current_user: User = Depends(get_current_active_user)) -> Category:
    category = category_service.create_category(category_create)
    return category


@has_role([Role.ADMIN])
@router.put("/category/{category_id}", response_model=Category)
def update_category(category_id: int, category_update: CategoryUpdate, category_service: CategoryService = Depends(),
                    current_user: User = Depends(get_current_active_user)) -> Type[Category]:
    category = category_service.update_category(category_id, category_update)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@has_role([Role.ADMIN])
@router.delete("/category/{category_id}", response_model=Category)
def delete_category(category_id: int, category_service: CategoryService = Depends(),
                    current_user: User = Depends(get_current_active_user)) -> Type[Category]:
    category = category_service.delete_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category
