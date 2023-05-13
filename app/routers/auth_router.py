from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.config.settings import settings
from app.dependencies.services import get_user_service
from app.dependencies.auth import get_current_active_user
from app.models.user import User
from app.schemas.token_schema import Token
from app.schemas.user_schema import UserCreate, UserBase
from app.services.user_service import UserService
from app.utils.auth_utils import create_access_token, authenticate_user

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        user_service: Annotated[UserService, Depends(get_user_service)]
):

    user = user_service.get_user_by_email(form_data.username)
    user = authenticate_user(user, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me", response_model=UserBase)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user_data: UserCreate,
                  user_service: Annotated[UserService, Depends(get_user_service)]) -> UserBase:
    created_user = user_service.create_user(user_data)
    return created_user
