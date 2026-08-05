from datetime import date
from decimal import Decimal

from app.repositories.dashboard import DashboardRepository
from app.schemas.dashboard import (
    DashboardCategoryResponse,
    DashboardMonthlyResponse,
    DashboardRegionResponse,
    DashboardSummaryResponse,
    DashboardTopProductResponse,
)


class DashboardService:
    def __init__(
        self,
        repository: DashboardRepository,
    ):
        self.repository = repository

    def get_summary(
        self,
        start_date: date | None = None,
        end_date: date | None = None,
        category: str | None = None,
        region: str | None = None,
    ) -> DashboardSummaryResponse:
        (
            total_orders,
            total_quantity,
            total_revenue,
            average_order_value,
        ) = self.repository.get_summary(
            start_date,
            end_date,
            category,
            region,
        )

        return DashboardSummaryResponse(
            total_orders=total_orders,
            total_quantity=total_quantity,
            total_revenue=total_revenue.quantize(
                Decimal("0.01"),
            ),
            average_order_value=average_order_value.quantize(
                Decimal("0.01"),
            ),
        )

    def get_revenue_by_category(
        self,
        start_date: date | None = None,
        end_date: date | None = None,
        category: str | None = None,
        region: str | None = None,
    ) -> list[DashboardCategoryResponse]:
        rows = self.repository.get_revenue_by_category(
            start_date,
            end_date,
            category,
            region,
        )

        return [
            DashboardCategoryResponse(
                category=row.category,
                total_revenue=row.total_revenue.quantize(
                    Decimal("0.01"),
                ),
                total_quantity=row.total_quantity,
            )
            for row in rows
        ]

    def get_revenue_by_region(
        self,
        start_date: date | None = None,
        end_date: date | None = None,
        category: str | None = None,
        region: str | None = None,
    ) -> list[DashboardCategoryResponse]:
        rows = self.repository.get_revenue_by_region(
            start_date,
            end_date,
            category,
            region,
        )

        return [
            DashboardRegionResponse(
                region=row.region,
                total_revenue=row.total_revenue.quantize(
                    Decimal("0.01"),
                ),
                total_quantity=row.total_quantity,
            )
            for row in rows
        ]

    def get_monthly_revenue(
        self,
        start_date: date | None = None,
        end_date: date | None = None,
        category: str | None = None,
        region: str | None = None,
    ) -> list[DashboardCategoryResponse]:
        rows = self.repository.get_monthly_revenue(
            start_date,
            end_date,
            category,
            region,
        )

        return [
            DashboardMonthlyResponse(
                month=row.month,
                total_revenue=row.total_revenue.quantize(
                    Decimal("0.01"),
                ),
                total_orders=row.total_orders,
            )
            for row in rows
        ]

    def get_top_products(
        self,
        start_date: date | None = None,
        end_date: date | None = None,
        category: str | None = None,
        region: str | None = None,
        limit: int = 10,
    ):
        rows = self.repository.get_top_products(
            start_date,
            end_date,
            category,
            region,
            limit,
        )

        return [
            DashboardTopProductResponse(
                product_name=row.product_name,
                total_quantity=row.total_quantity,
                total_revenue=row.total_revenue,
            )
            for row in rows
        ]
