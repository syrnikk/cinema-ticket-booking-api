from pydantic import BaseModel


class ResetPasswordRequest(BaseModel):
    email: str
    reset_token: str
    new_password: str


class ResetPasswordResponse(BaseModel):
    success: bool
    message: str


class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str


class ChangePasswordResponse(BaseModel):
    success: bool
    message: str
