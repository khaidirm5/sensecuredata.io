from sqlalchemy import Select, delete, func, or_, select
from sqlalchemy.orm import Session

from app.models.sales_data import SalesData
from app.schemas.sales import SalesCreate, SalesUpdate


class SalesRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        data: SalesCreate,
    ) -> SalesData:
        sale = SalesData(**data.model_dump())

        self.db.add(sale)
        self.db.commit()
        self.db.refresh(sale)

        return sale

    def get_by_id(
        self,
        sale_id: int,
    ) -> SalesData | None:
        stmt: Select[tuple[SalesData]] = select(SalesData).where(
            SalesData.id == sale_id
        )

        return self.db.scalar(stmt)

    def get_all(
        self,
        *,
        skip: int = 0,
        limit: int = 20,
        search: str | None = None,
        category: str | None = None,
        region: str | None = None,
        sort_by: str = "order_date",
        order: str = "desc",
    ) -> list[SalesData]:

        stmt: Select[tuple[SalesData]] = select(SalesData)

        if search:
            keyword = f"%{search}%"

            stmt = stmt.where(
                or_(
                    SalesData.invoice_number.ilike(keyword),
                    SalesData.product_name.ilike(keyword),
                    SalesData.category.ilike(keyword),
                    SalesData.region.ilike(keyword),
                )
            )

        if category:
            stmt = stmt.where(SalesData.category == category)

        if region:
            stmt = stmt.where(SalesData.region == region)

        allowed_sort = {
            "order_date": SalesData.order_date,
            "invoice_number": SalesData.invoice_number,
            "product_name": SalesData.product_name,
            "quantity": SalesData.quantity,
            "total_price": SalesData.total_price,
            "region": SalesData.region,
            "category": SalesData.category,
            "unit_price": SalesData.unit_price,
            "created_at": SalesData.created_at,
        }

        column = allowed_sort.get(
            sort_by,
            SalesData.order_date,
        )

        stmt = stmt.order_by(column.desc() if order.lower() == "desc" else column.asc())

        stmt = stmt.offset(skip).limit(limit)

        return list(self.db.scalars(stmt).all())

    def count(
        self,
        *,
        search: str | None = None,
        category: str | None = None,
        region: str | None = None,
    ) -> int:
        stmt = select(func.count()).select_from(SalesData)

        if search:
            keyword = f"%{search}"

            stmt = stmt.where(
                or_(
                    SalesData.invoice_number.ilike(keyword),
                    SalesData.product_name.ilike(keyword),
                    SalesData.category.ilike(keyword),
                    SalesData.region.ilike(keyword),
                )
            )

        if category:
            stmt = stmt.where(SalesData.category == category)

        if region:
            stmt = stmt.where(SalesData.region == region)

        return self.db.scalar(stmt) or 0

    def update(
        self,
        sale: SalesData,
        data: SalesUpdate,
    ) -> SalesData:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(sale, key, value)

        self.db.commit()
        self.db.refresh(sale)

        return sale

    def delete(
        self,
        sale_id: int,
    ) -> None:
        stmt = delete(SalesData).where(SalesData.id == sale_id)

        self.db.execute(stmt)
        self.db.commit()
