from sqlalchemy import Select, asc, desc, func, or_, select
from sqlalchemy.orm import Session

from app.models.sales_data import SalesData
from app.schemas.sales import SalesCreate, SalesUpdate


class SalesRepository:
    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        data: SalesCreate,
    ) -> SalesData:
        sale = SalesData(
            **data.model_dump(),
        )

        self.db.add(sale)
        self.db.commit()
        self.db.refresh(sale)

        return sale

    def get_by_id(
        self,
        sale_id: int,
    ) -> SalesData | None:
        stmt = select(SalesData).where(
            SalesData.id == sale_id,
        )

        return self.db.execute(stmt).scalar_one_or_none()

    def _apply_filters(
        self,
        stmt: Select,
        search: str | None = None,
        category: str | None = None,
        region: str | None = None,
    ) -> Select:
        if search:
            search_pattern = f"%{search.strip()}%"

            stmt = stmt.where(
                or_(
                    SalesData.invoice_number.ilike(search_pattern),
                    SalesData.product_name.ilike(search_pattern),
                    SalesData.category.ilike(search_pattern),
                    SalesData.region.ilike(search_pattern),
                )
            )

        if category:
            category_pattern = f"%{category.strip()}%"

            stmt = stmt.where(
                SalesData.category.ilike(
                    category_pattern,
                ),
            )

        if region:
            region_pattern = f"%{region.strip()}%"

            stmt = stmt.where(
                SalesData.region.ilike(
                    region_pattern,
                ),
            )

        return stmt

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
        sort_column = getattr(
            SalesData,
            sort_by,
            SalesData.order_date,
        )

        if order == "asc":
            sort_expression = asc(sort_column)
        else:
            sort_expression = desc(sort_column)

        stmt = select(SalesData)

        stmt = self._apply_filters(
            stmt,
            search=search,
            category=category,
            region=region,
        )

        stmt = (
            stmt.order_by(
                sort_expression,
                desc(SalesData.id),
            )
            .offset(skip)
            .limit(limit)
        )

        return list(self.db.execute(stmt).scalars().all())

    def count(
        self,
        *,
        search: str | None = None,
        category: str | None = None,
        region: str | None = None,
    ) -> int:
        stmt = select(func.count(SalesData.id))

        stmt = self._apply_filters(
            stmt,
            search=search,
            category=category,
            region=region,
        )

        return self.db.execute(stmt).scalar_one()

    def update(
        self,
        sale: SalesData,
        data: SalesUpdate,
    ) -> SalesData:
        update_data = data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                sale,
                field,
                value,
            )

        self.db.commit()
        self.db.refresh(sale)

        return sale

    def delete(
        self,
        sale_id: int,
    ) -> None:
        sale = self.get_by_id(sale_id)

        if sale is None:
            return

        self.db.delete(sale)
        self.db.commit()
