from decimal import Decimal

from app.repositories.dashboard import DashboardRepository
from app.schemas.dashboard import DashboardSummaryResponse


class DashboardService:
    def __init__(
        self,
        repository: DashboardRepository,
    ):
        self.repository = repository

    def get_summary(
        self,
    ) -> DashboardSummaryResponse:
        (
            total_orders,
            total_quantity,
            total_revenue,
            average_order_value,
        ) = self.repository.get_summary()

        if isinstance(total_revenue, Decimal):
            total_revenue = total_revenue.quantize(Decimal("0.01"))

        if isinstance(average_order_value, Decimal):
            average_order_value = average_order_value.quantize(Decimal("0.01"))

        return DashboardSummaryResponse(
            total_orders=total_orders,
            total_quantity=total_quantity,
            total_revenue=total_revenue,
            average_order_value=average_order_value,
        )
