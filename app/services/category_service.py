from typing import List, Type

from fastapi import Depends
from fastapi_pagination import Page, Params

from app.models import Category
from app.repositories.category_repository import CategoryRepository
from app.schemas.category_schema import CategoryCreate, CategoryUpdate


class CategoryService:
    def __init__(self, category_repository: CategoryRepository = Depends()):
        self.category_repository = category_repository

    def get_category(self, category_id: int) -> Type[Category] | None:
        return self.category_repository.get_category(category_id)

    def get_categories(self) -> Page[Category]:
        return self.category_repository.get_categories()

    def create_category(self, category_create: CategoryCreate) -> Category:
        return self.category_repository.create_category(category_create)

    def update_category(self, category_id: int, category_update: CategoryUpdate) -> Type[Category] | None:
        return self.category_repository.update_category(category_id, category_update)

    def delete_category(self, category_id: int) -> Type[Category] | None:
        return self.category_repository.delete_category(category_id)
