from sqlalchemy import Boolean, CheckConstraint, DateTime, Integer, String, text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    __table_args__ = (
        CheckConstraint(
            "role IN ('admin', 'analyst', 'user')",
            name="chk_users_role",
        ),
    )

    id = mapped_column(
        Integer,
        primary_key=True,
    )

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    role: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        server_default=text("'user'"),
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    last_login = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
