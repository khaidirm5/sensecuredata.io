from datetime import datetime

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.db.base import Base


class UploadHistory(Base):
    __tablename__ = "upload_history"

    __table_args__ = (
        CheckConstraint(
            "status IN ('PENDING', 'PROCESSING', 'SUCCESS', 'FAILED')",
            name="chk_upload_status",
        ),
        CheckConstraint(
            "file_type IN ('csv', 'xlsx')",
            name="chk_upload_file_type",
        ),
        CheckConstraint(
            "total_rows >= 0",
            name="chk_total_rows",
        ),
        CheckConstraint(
            "invalid_rows >= 0",
            name="chk_invalid_rows",
        ),
        Index(
            "idx_upload_history_uploaded_at",
            "uploaded_at",
        ),
        Index(
            "idx_upload_history_uploaded_by",
            "uploaded_by",
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    uploaded_by: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    file_type: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    total_rows: Mapped[int] = mapped_column(
        Integer,
        server_default=text("0"),
        nullable=False,
    )

    valid_rows: Mapped[int] = mapped_column(
        Integer,
        server_default=text("0"),
        nullable=False,
    )

    invalid_rows: Mapped[int] = mapped_column(
        Integer,
        server_default=text("0"),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        server_default=text("'PENDING'"),
        nullable=False,
    )

    error_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    security_scans = relationship(
        "SecurityScan",
        back_populates="upload",
        cascade="all, delete-orphan",
    )
