from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    CheckConstraint,
    Date,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    UniqueConstraint,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class SalesData(Base):
    __tablename__ = "sales_data"

    __table_args__ = (
        Index("idx_sales_invoice", "invoice_number"),
        Index("idx_sales_category", "category"),
        Index("idx_sales_order_date", "order_date"),
        Index("idx_sales_region", "region"),
        Index("idx_sales_upload", "upload_id"),
        Index("idx_sales_date_category", "order_date", "category"),
        Index("idx_sales_date_region", "order_date", "region"),
        UniqueConstraint(
            "upload_id",
            "invoice_number",
            "product_name",
            name="uq_sales_record",
        ),
        CheckConstraint(
            "quantity >= 0",
            name="sales_data_quantity_check",
        ),
        CheckConstraint(
            "unit_price >= 0",
            name="sales_data_unit_price_check",
        ),
        CheckConstraint(
            "total_price >= 0",
            name="sales_data_total_price_check",
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    upload_id: Mapped[int] = mapped_column(
        ForeignKey("upload_history.id", ondelete="CASCADE"),
        nullable=False,
    )

    invoice_number: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    order_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    product_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    unit_price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    total_price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    region: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
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
