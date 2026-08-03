from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.repositories.user import (
    create_user,
    get_user_by_email,
    get_user_by_username,
)
from app.schemas.user import (
    Token,
    TokenPair,
    UserCreate,
)
from app.security.hash import hash_password, verify_password
from app.security.jwt import (
    create_access_token,
    create_refresh_token,
    decode_refresh_token,
)


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
) -> TokenPair:
    """Authenticate a user and return access and refresh tokens."""

    user = get_user_by_email(db, email)

    if user is None:
        raise ValueError("Invalid email or password.")

    if not verify_password(password, user.hashed_password):
        raise ValueError("Invalid email or password.")

    user.last_login = datetime.now(timezone.utc)
    db.commit()
    db.refresh(user)

    access_token = create_access_token(
        {
            "sub": str(user.id),
        }
    )

    refresh_token = create_refresh_token(
        {
            "sub": str(user.id),
        }
    )

    return TokenPair(
        access_token=access_token,
        refresh_token=refresh_token,
    )


def refresh_access_token(
    refresh_token: str,
) -> Token:
    """Generate a new access token from a refresh token."""

    try:
        payload = decode_refresh_token(refresh_token)
    except ValueError as exc:
        raise ValueError("Invalid or expired refresh token.") from exc

    access_token = create_access_token(
        {
            "sub": payload["sub"],
        }
    )

    return Token(
        access_token=access_token,
    )
