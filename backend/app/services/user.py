from sqlalchemy.orm import Session

from app.repositories.user import (
    create_user,
    get_user_by_email,
    get_user_by_username,
)
from app.schemas.user import UserCreate
from app.security.hash import hash_password


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
