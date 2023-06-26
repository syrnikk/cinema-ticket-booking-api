from datetime import datetime
import pytest
from app.models.user import Role, User
from app.routers.user_router import change_password, delete_logged_in_user_account, update_user
from app.schemas.password_schema import ChangePasswordRequest, ChangePasswordResponse
from app.schemas.response_schema import MessageResponse
from app.schemas.user_schema import UserUpdate

from tests.mocks.user_router_mock import MockUser, MockUserService


def test_change_password():
    user_service = MockUserService()

    request = ChangePasswordRequest(old_password="old_password", new_password="new_password")
    current_user = MockUser()

    result = change_password(request, current_user=current_user, user_service=user_service)

    assert result is not None
    assert isinstance(result, ChangePasswordResponse)
    assert result.success is True
    assert result.message == "Password changed successfully"

def test_delete_logged_in_user_account():
    user_service = MockUserService()

    user_id = 1
    current_user = MockUser()

    result = delete_logged_in_user_account(user_id, user_service=user_service, current_user=current_user)

    assert result is not None
    assert isinstance(result, MessageResponse)
    assert result.message == "User deleted successfully"

def test_update_user():
    user_service = MockUserService()

    user_id = 1
    user_update = UserUpdate(
        first_name="Updated",
        last_name="User",
        email="updated@example.com"
    )

    current_user = MockUser()

    result = update_user(user_id, user_update, user_service=user_service, current_user=current_user)

    assert result is not None
    assert isinstance(result, User)
    assert result.first_name == "Updated"
    assert result.last_name == "User"
    assert result.email == "updated@example.com"