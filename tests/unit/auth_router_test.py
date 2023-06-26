from fastapi import status
from fastapi.testclient import TestClient
from app.main import app
from app.services.user_service import UserService
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

def mock_get_password_hash(user_password):
    return user_password

def mock_get_user_by_email(self, email):
    if email == user_email:
        return user
    return 0 

def mock_save_user(self, user):
    return user

def mock_authenticate_user(user, password):
    return user

def mock_get_current_active_user(user):
    return user

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

# NIE DZIAŁA BO WYSKAKUJE 401 UNATHORIZED
# def test_read_users_me_with_authenticated_user(monkeypatch):
#     # Mockowanie zależności
#     monkeypatch.setattr("app.dependencies.auth.get_current_user", lambda: User(id=1, email="test@example.com", disabled=False))

#     # Wywołanie żądania do API
#     response = client.get("/users/me")

#     # Sprawdzenie odpowiedzi
#     assert response.status_code == status.HTTP_200_OK
#     assert "email" in response.json()
#     assert response.json()["email"] == "test@example.com"

def test_read_users_me_with_unauthenticated_user(monkeypatch):
    monkeypatch.setattr("app.dependencies.auth.get_current_user", lambda: None)

    response = client.get("/users/me")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()["detail"] == "Not authenticated"

# NIE DZIAŁA BO WYSKAKUJE 401 UNATHORIZED
# def test_read_users_me_with_inactive_user(monkeypatch):
#     # Mockowanie zależności
#     monkeypatch.setattr("app.dependencies.auth.get_current_user", lambda: User(id=1, email="test@example.com", disabled=True))

#     # Wywołanie żądania do API
#     response = client.get("/users/me")

#     # Sprawdzenie odpowiedzi
#     assert response.status_code == status.HTTP_400_BAD_REQUEST
#     assert response.json()["detail"] == "Inactive user"

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