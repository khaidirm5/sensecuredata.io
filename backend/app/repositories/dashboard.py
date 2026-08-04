from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.sales_data import SalesData


class DashboardRepository:
    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def get_summary(self) -> tuple[int, int, object, object]:
        stmt = select(
            func.count(SalesData.id),
            func.coalesce(
                func.sum(SalesData.quantity),
                0,
            ),
            func.coalesce(
                func.sum(SalesData.total_price),
                0,
            ),
            func.coalesce(
                func.avg(SalesData.total_price),
                0,
            ),
        )

        return self.db.execute(stmt).one()
