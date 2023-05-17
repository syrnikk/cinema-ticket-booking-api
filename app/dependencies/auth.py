from functools import wraps

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from app.config.settings import settings
from app.models.user import User
from app.services.user_service import UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme),
                           user_service: UserService = Depends()):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = user_service.get_user_by_email(email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
        current_user: User = Depends(get_current_user)
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def has_role(roles: list[str]):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            current_user = kwargs['current_user']
            if not any(role == current_user.role for role in roles):
                raise HTTPException(status_code=403, detail="Insufficient role")
            return await func(*args, **kwargs)
        return wrapper
    return decorator
