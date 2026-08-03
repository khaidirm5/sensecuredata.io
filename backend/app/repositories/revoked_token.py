from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.revoked_token import RevokedToken


def revoke_token(
    db: Session,
    jti: str,
    expires_at: datetime,
) -> RevokedToken:
    """Store a revoked JWT."""

    revoked_token = RevokedToken(
        jti=jti,
        expires_at=expires_at,
    )

    db.add(revoked_token)
    db.commit()
    db.refresh(revoked_token)

    return revoked_token


def is_token_revoked(
    db: Session,
    jti: str,
) -> bool:
    """Check whether a JWT has been revoked."""

    stmt = select(RevokedToken).where(
        RevokedToken.jti == jti,
    )

    return db.scalar(stmt) is not None
