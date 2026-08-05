from datetime import datetime

from sqlalchemy import (
    JSON,
    BigInteger,
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class SecurityScan(Base):
    __tablename__ = "security_scans"

    __table_args__ = (
        CheckConstraint(
            "security_score BETWEEN 0 AND 100",
            name="chk_security_score",
        ),
        CheckConstraint(
            "risk_level IN ('SAFE', 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL')",
            name="chk_risk_level",
        ),
        CheckConstraint(
            "status IN ('PENDING', 'SCANNING', 'COMPLETED', 'FAILED')",
            name="chk_security_status",
        ),
        CheckConstraint(
            """
            threat_type IN (
                'NONE',
                'MALWARE',
                'MACRO',
                'EXECUTABLE',
                'SUSPICIOUS',
                'UNKNOWN'
            )
            """,
            name="chk_security_threat",
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    upload_id: Mapped[int] = mapped_column(
        ForeignKey(
            "upload_history.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    file_hash: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )

    mime_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    extension: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    file_size: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    is_duplicate: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    risk_level: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    security_score: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    scan_details: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    threat_type: Mapped[str] = mapped_column(
        String(50),
        default="NONE",
        nullable=False,
    )

    scan_duration_ms: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    scanner_version: Mapped[str] = mapped_column(
        String(20),
        default="v1.0",
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    upload = relationship(
        "UploadHistory",
        back_populates="security_scans",
    )
