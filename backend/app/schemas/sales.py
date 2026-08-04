from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class SalesBase(BaseModel):
    invoice_number: str
    order_date: date
    product_name: str
    category: str
    quantity: int
    unit_price: Decimal
    total_price: Decimal
    region: str | None = None


class SalesCreate(SalesBase):
    upload_id: int


class SalesUpdate(BaseModel):
    invoice_number: str | None = None
    order_date: date | None = None
    product_name: str | None = None
    category: str | None = None
    quantity: int | None = None
    unit_price: Decimal | None = None
    total_price: Decimal | None = None
    region: str | None = None


class SalesResponse(SalesBase):
    id: int
    upload_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
