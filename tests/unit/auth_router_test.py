from fastapi import status
from fastapi.testclient import TestClient
from app.main import app
from app.services.user_service import UserService
from tests.mocks.auth_router_mock import mock_authenticate_user, mock_get_user_by_email, user_email, user_password

client = TestClient(app)

def test_login_for_access_token_with_valid_credentials(monkeypatch):
    monkeypatch.setattr(UserService, "get_user_by_email", mock_get_user_by_email)
    monkeypatch.setattr("app.utils.auth_utils.authenticate_user", mock_authenticate_user)

    response = client.post(
        "/token",
        data={
            "username": user_email,
            "password": user_password,
        },
    )

    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_for_access_token_with_invalid_credentials(monkeypatch):
    monkeypatch.setattr(UserService, "get_user_by_email", mock_get_user_by_email)
    monkeypatch.setattr("app.utils.auth_utils.authenticate_user", mock_authenticate_user)

    response = client.post(
        "/token",
        data={
            "username": "invalid@example.com",
            "password": "invalidpassword",
        },
    )
    assert response.status_code == 401
    assert response.json().get("detail") == "Incorrect username or password"
    assert response.headers.get("WWW-Authenticate") == "Bearer"

def test_read_users_me_with_unauthenticated_user(monkeypatch):
    monkeypatch.setattr("app.dependencies.auth.get_current_user", lambda: None)

    response = client.get("/users/me")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()["detail"] == "Not authenticated"

def test_reset_password_with_existing_user(monkeypatch):
    monkeypatch.setattr(UserService, "get_user_by_email", mock_get_user_by_email)
    monkeypatch.setattr(UserService, "reset_password", lambda self, user, reset_token, new_password: None)

    response = client.post("/reset-password", json={"email": user_email, "reset_token": "token123", "new_password": "newpassword"})

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"success": True, "message": "Changed password successfully"}

def test_reset_password_with_non_existing_user(monkeypatch):
    monkeypatch.setattr(UserService, "get_user_by_email", lambda self, email: None)

    response = client.post("/reset-password", json={"email": "nonexisting@example.com", "reset_token": "token123", "new_password": "newpassword"})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "User with given email not found"}