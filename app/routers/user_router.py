from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.auth import get_current_active_user
from app.models.user import User, Role
from app.schemas import user_schema
from app.schemas.password_schema import ChangePasswordRequest, ChangePasswordResponse
from app.schemas.response_schema import MessageResponse
from app.schemas.user_schema import UserUpdate

from app.services.user_service import UserService

router = APIRouter(tags=["User"])


@router.post("/change-password")
async def change_password(request: ChangePasswordRequest,
                          current_user: User = Depends(get_current_active_user),
                          user_service: UserService = Depends()):
    if user_service.change_password(current_user, request.old_password, request.new_password):
        return ChangePasswordResponse(success=True, message="Password changed successfully")
    else:
        raise HTTPException(status_code=400, detail="Invalid password")


@router.delete("/users/{user_id}")
def delete_logged_in_user_account(user_id: int, user_service: UserService = Depends(),
                                  current_user: User = Depends(get_current_active_user)):
    if current_user.id != user_id and current_user.role != Role.ADMIN:
        raise HTTPException(status_code=403, detail="Cannot delete another user's account")
    user_service.delete_user(current_user)
    return MessageResponse(message="User deleted successfully")


@router.put("/users/{user_id}", response_model=user_schema.User)
def update_user(
    user_id: int,
    user_update: UserUpdate,
    user_service: UserService = Depends(),
    current_user: User = Depends(get_current_active_user)
):
    if current_user.id != user_id and current_user.role != Role.ADMIN:
        raise HTTPException(status_code=403, detail="Cannot update another user's account")
    user = user_service.update_user(user_id, user_update)
    return user
