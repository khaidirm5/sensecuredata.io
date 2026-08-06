from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.models.security_scan import SecurityScan


class DuplicateDetector:
    @staticmethod
    def is_duplicate(
        db: Session,
        file_hash: str,
    ) -> bool:
        stmt: Select[tuple[SecurityScan]] = select(SecurityScan).where(
            SecurityScan.file_hash == file_hash,
        )

        return db.scalar(stmt) is not None
