from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    """Schema for user registration requests."""

    username: str = Field(
        min_length=3,
        max_length=50,
    )
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=255,
    )


class UserResponse(BaseModel):
    """Schema returned after creating or retrieving a user."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    is_active: bool


class UserLogin(BaseModel):
    """Schema for user login requests."""

    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=255,
    )


class Token(BaseModel):
    """Schema returned after successful authentication."""

    access_token: str
    token_type: str = "bearer"
