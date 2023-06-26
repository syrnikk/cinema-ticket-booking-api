from app.models.user import Role, User
from app.schemas.response_schema import MessageResponse

class MockUserService:
    def change_password(self, user, old_password, new_password):
        if old_password == "old_password" and new_password == "new_password":
            return True
        return False
    
    def delete_user(self, user):
        return MessageResponse(message="User deleted successfully")

    def update_user(self, user_id, user_update):
        current_user = self.get_user(user_id)
        if current_user:
            if user_update.first_name:
                current_user.first_name = user_update.first_name
            if user_update.last_name:
                current_user.last_name = user_update.last_name
            if user_update.date_of_birth:
                current_user.date_of_birth = user_update.date_of_birth
            if user_update.email:
                current_user.email = user_update.email
            if user_update.phone:
                current_user.phone = user_update.phone
            if user_update.image_url:
                current_user.image_url = user_update.image_url
            return current_user
        else:
            return None

    def get_user(self, user_id):
        return User(id=user_id, first_name="John", last_name="Doe", email="john@example.com")

class MockUser:
    id = 1
    role = Role.ADMIN