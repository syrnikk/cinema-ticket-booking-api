from app.models.user import Role, User
from app.utils.auth_utils import get_password_hash


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