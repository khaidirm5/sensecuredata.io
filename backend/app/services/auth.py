from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.repositories.revoked_token import revoke_token
from app.security.jwt import decode_access_token


def logout(
    db: Session,
    token: str,
) -> None:
    """Revoke an access token."""

    payload = decode_access_token(token)

    revoke_token(
        db=db,
        jti=payload["jti"],
        expires_at=datetime.fromtimestamp(
            payload["exp"],
            tz=timezone.utc,
        ),
    )
