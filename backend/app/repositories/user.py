from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


def get_user_by_email(db: Session, email: str) -> User | None:
    """Retrieve a user by email."""

    stmt = select(User).where(User.email == email)
    return db.scalar(stmt)


def get_user_by_username(db: Session, username: str) -> User | None:
    """Retrieve a user by username."""

    stmt = select(User).where(User.username == username)
    return db.scalar(stmt)


def get_user_by_id(db: Session, user_id: int) -> User | None:
    """Retrieve a user by ID."""

    stmt = select(User).where(User.id == user_id)
    return db.scalar(stmt)


def create_user(
    db: Session,
    username: str,
    email: str,
    hashed_password: str,
) -> User:
    """Create a new user."""

    user = User(
        username=username,
        email=email,
        hashed_password=hashed_password,
        role="user",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
