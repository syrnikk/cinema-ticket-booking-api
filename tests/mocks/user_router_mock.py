from app.models.user import Role, User
from app.schemas.response_schema import MessageResponse

class MockUserService:
    async def change_password(self, user, old_password, new_password):
        if old_password == "old_password" and new_password == "new_password":
            return True
        return False
    
    async def delete_user(self, user):
        # Tutaj możesz dodać logikę usuwania użytkownika
        return MessageResponse(message="User deleted successfully")

    async def update_user(self, user_id, user_update):
        # Tutaj możesz dodać logikę aktualizacji użytkownika
        updated_user = User(id=user_id, username=user_update.username, email=user_update.email)
        return updated_user

class MockUser:
    id = 1
    role = Role.ADMIN