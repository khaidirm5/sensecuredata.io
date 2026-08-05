from datetime import date
from decimal import Decimal

from sqlalchemy import Select, desc, func, select
from sqlalchemy.orm import Session

from app.models.sales_data import SalesData


class DashboardRepository:
    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def _apply_filters(
        self,
        stmt: Select,
        start_date: date | None = None,
        end_date: date | None = None,
        category: str | None = None,
        region: str | None = None,
    ) -> Select:
        if start_date:
            stmt = stmt.where(
                SalesData.order_date >= start_date,
            )

        if end_date:
            stmt = stmt.where(
                SalesData.order_date <= end_date,
            )

        if category:
            stmt = stmt.where(
                SalesData.category == category,
            )

        if region:
            stmt = stmt.where(
                SalesData.region == region,
            )

        return stmt

    def get_summary(
        self,
        start_date: date | None = None,
        end_date: date | None = None,
        category: str | None = None,
        region: str | None = None,
    ) -> tuple[int, int, Decimal, Decimal]:
        stmt = select(
            func.count(SalesData.id).label("total_orders"),
            func.coalesce(
                func.sum(SalesData.quantity),
                0,
            ).label("total_quantity"),
            func.coalesce(
                func.sum(SalesData.total_price),
                0,
            ).label("total_revenue"),
            func.coalesce(
                func.avg(SalesData.total_price),
                0,
            ).label("average_order_value"),
        )

        stmt = self._apply_filters(
            stmt,
            start_date,
            end_date,
            category,
            region,
        )

        result = self.db.execute(stmt).one()

        return (
            result.total_orders,
            result.total_quantity,
            result.total_revenue,
            result.average_order_value,
        )

    def get_revenue_by_category(
        self,
        start_date: date | None = None,
        end_date: date | None = None,
        category: str | None = None,
        region: str | None = None,
    ):
        stmt = (
            select(
                SalesData.category,
                func.coalesce(
                    func.sum(SalesData.total_price),
                    0,
                ).label("total_revenue"),
                func.coalesce(
                    func.sum(SalesData.quantity),
                    0,
                ).label("total_quantity"),
            )
            .group_by(
                SalesData.category,
            )
            .order_by(
                desc("total_revenue"),
            )
        )

        stmt = self._apply_filters(
            stmt,
            start_date,
            end_date,
            category,
            region,
        )

        return self.db.execute(stmt).all()

    def get_revenue_by_region(
        self,
        start_date: date | None = None,
        end_date: date | None = None,
        category: str | None = None,
        region: str | None = None,
    ):
        stmt = (
            select(
                SalesData.region,
                func.coalesce(
                    func.sum(SalesData.total_price),
                    0,
                ).label("total_revenue"),
                func.coalesce(
                    func.sum(SalesData.quantity),
                    0,
                ).label("total_quantity"),
            )
            .group_by(
                SalesData.region,
            )
            .order_by(
                desc("total_revenue"),
            )
        )

        stmt = self._apply_filters(
            stmt,
            start_date,
            end_date,
            category,
            region,
        )

        return self.db.execute(stmt).all()

    def get_monthly_revenue(
        self,
        start_date: date | None = None,
        end_date: date | None = None,
        category: str | None = None,
        region: str | None = None,
    ):
        stmt = (
            select(
                func.to_char(
                    SalesData.order_date,
                    "YYYY-MM",
                ).label("month"),
                func.coalesce(
                    func.sum(SalesData.total_price),
                    0,
                ).label("total_revenue"),
                func.count(
                    SalesData.id,
                ).label("total_orders"),
            )
            .group_by(
                func.to_char(
                    SalesData.order_date,
                    "YYYY-MM",
                )
            )
            .order_by("month")
        )

        stmt = self._apply_filters(
            stmt,
            start_date,
            end_date,
            category,
            region,
        )

        return self.db.execute(stmt).all()

    def get_top_products(
        self,
        start_date: date | None = None,
        end_date: date | None = None,
        category: str | None = None,
        region: str | None = None,
        limit: int = 10,
    ):
        stmt = select(
            SalesData.product_name,
            func.coalesce(
                func.sum(SalesData.quantity),
                0,
            ).label("total_quantity"),
            func.coalesce(
                func.sum(SalesData.total_price),
                0,
            ).label("total_revenue"),
        ).group_by(
            SalesData.product_name,
        )

        stmt = self._apply_filters(
            stmt,
            start_date,
            end_date,
            category,
            region,
        )

        stmt = stmt.order_by(
            desc("total_quantity"),
        ).limit(limit)

        return self.db.execute(stmt).all()
