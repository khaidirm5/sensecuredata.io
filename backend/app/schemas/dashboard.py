from decimal import Decimal

from pydantic import BaseModel


class DashboardSummaryResponse(BaseModel):
    total_orders: int
    total_quantity: int
    total_revenue: Decimal
    average_order_value: Decimal


class DashboardCategoryResponse(BaseModel):
    category: str
    total_revenue: Decimal
    total_quantity: int


class DashboardRegionResponse(BaseModel):
    region: str | None
    total_revenue: Decimal
    total_quantity: int


class DashboardMonthlyResponse(BaseModel):
    month: str
    total_revenue: Decimal
    total_orders: int


class DashboardTopProductResponse(BaseModel):
    product_name: str
    total_quantity: int
    total_revenue: Decimal
