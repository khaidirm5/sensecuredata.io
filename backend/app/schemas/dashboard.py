from decimal import Decimal

from pydantic import BaseModel


class DashboardSummaryResponse(BaseModel):
    total_orders: int
    total_quantity: int
    total_revenue: Decimal
    average_order_value: Decimal
