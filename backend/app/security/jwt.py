from datetime import datetime, timedelta, timezone
from typing import Any
from uuid import uuid4

from jose import JWTError, jwt

from app.config.settings import settings


def create_access_token(
    data: dict[str, Any],
    expires_delta: timedelta | None = None,
) -> str:
    """Create a signed JWT access token."""

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + (
        expires_delta
        if expires_delta is not None
        else timedelta(minutes=settings.access_token_expire_minutes)
    )

    to_encode["exp"] = expire
    to_encode["type"] = "access"
    to_encode["jti"] = str(uuid4())

    return jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm,
    )


def create_refresh_token(
    data: dict[str, Any],
    expires_delta: timedelta | None = None,
) -> str:
    """Create a signed JWT refresh token."""

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + (
        expires_delta if expires_delta is not None else timedelta(days=7)
    )

    to_encode["exp"] = expire
    to_encode["type"] = "refresh"
    to_encode["jti"] = str(uuid4())
    return jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm,
    )


def decode_token(token: str) -> dict[str, Any]:
    """Validate and decode a JWT."""

    try:
        return jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm],
        )
    except JWTError as exc:
        raise ValueError("Invalid or expired token.") from exc


def decode_access_token(token: str) -> dict[str, Any]:
    """Validate and decode an access token."""

    payload = decode_token(token)

    if payload.get("type") != "access":
        raise ValueError("Invalid access token.")

    return payload


def decode_refresh_token(token: str) -> dict[str, Any]:
    """Validate and decode a refresh token."""

    payload = decode_token(token)

    if payload.get("type") != "refresh":
        raise ValueError("Invalid refresh token.")

    return payload
