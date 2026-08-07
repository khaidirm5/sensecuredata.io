from sqlalchemy import func, or_, select
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


def get_users(
    db: Session,
    *,
    page: int,
    limit: int,
    search: str | None = None,
    role: str | None = None,
    sort_by: str = "username",
    order: str = "asc",
) -> tuple[list[User], int]:
    """Retrieve users with pagination, search, filtering, and sorting."""

    stmt = select(User)
    count_stmt = select(func.count()).select_from(User)

    if search:
        condition = or_(
            User.username.ilike(f"%{search}%"),
            User.email.ilike(f"%{search}%"),
        )

        stmt = stmt.where(condition)
        count_stmt = count_stmt.where(condition)

    if role:
        stmt = stmt.where(User.role == role)
        count_stmt = count_stmt.where(User.role == role)

    sortable_columns = {
        "username": User.username,
        "email": User.email,
        "created_at": User.created_at,
    }

    sort_column = sortable_columns.get(sort_by, User.username)

    if order == "desc":
        stmt = stmt.order_by(sort_column.desc())
    else:
        stmt = stmt.order_by(sort_column.asc())

    total = db.scalar(count_stmt) or 0

    stmt = stmt.offset((page - 1) * limit).limit(limit)

    users = db.scalars(stmt).all()

    return users, total
