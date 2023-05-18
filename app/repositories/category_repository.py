from typing import Type

from fastapi import Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.models import Category
from app.schemas.category_schema import CategoryCreate, CategoryUpdate


class CategoryRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_category(self, category_id: int) -> Type[Category] | None:
        return self.db.query(Category).filter(Category.id == category_id).first()

    def get_categories(self) -> Page[Category]:
        query = self.db.query(Category)
        return paginate(query)

    def create_category(self, category_create: CategoryCreate) -> Category:
        category = Category(**category_create.dict())
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category

    def update_category(self, category_id: int, category_update: CategoryUpdate) -> Type[Category] | None:
        category = self.get_category(category_id)
        if category:
            for key, value in category_update.dict().items():
                setattr(category, key, value)
            self.db.commit()
            self.db.refresh(category)
        return category

    def delete_category(self, category_id: int) -> Type[Category] | None:
        category = self.get_category(category_id)
        if category:
            self.db.delete(category)
            self.db.commit()
        return category
