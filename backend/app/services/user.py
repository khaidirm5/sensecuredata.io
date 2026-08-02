from sqlalchemy.orm import Session

from app.repositories.user import (
    create_user,
    get_user_by_email,
    get_user_by_username,
)
from app.schemas.user import Token, UserCreate
from app.security.hash import hash_password, verify_password
from app.security.jwt import create_access_token


def register_user(db: Session, user: UserCreate):
    """Register a new user."""

    if get_user_by_email(db, user.email):
        raise ValueError("Email is already registered.")

    if get_user_by_username(db, user.username):
        raise ValueError("Username is already taken.")

    return create_user(
        db=db,
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
    )


def authenticate_user(
    db: Session,
    email: str,
    password: str,
) -> Token:
    """Authenticate a user and return an access token."""

    user = get_user_by_email(db, email)

    if user is None:
        raise ValueError("Invalid email or password.")

    if not verify_password(password, user.hashed_password):
        raise ValueError("Invalid email or password.")

    access_token = create_access_token(
        {
            "sub": str(user.id),
        }
    )

    return Token(
        access_token=access_token,
    )
