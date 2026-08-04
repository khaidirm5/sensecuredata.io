from sqlalchemy.orm import Session

from app.models.sales_data import SalesData


class DataLoader:
    """Load transformed sales data into database."""

    @classmethod
    def bulk_insert(
        cls,
        db: Session,
        sales: list[SalesData],
    ) -> int:
        if not sales:
            return 0

        db.bulk_save_objects(sales)

        return len(sales)
