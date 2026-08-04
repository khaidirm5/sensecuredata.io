from sqlalchemy import Select, delete, select
from sqlalchemy.orm import Session

from app.models.sales_data import SalesData
from app.schemas.sales import SalesCreate, SalesUpdate


class SalesRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: SalesCreate) -> SalesData:
        sale = SalesData(**data.model_dump())
        self.db.add(sale)
        self.db.commit()
        self.db.refresh(sale)
        return sale

    def get_by_id(self, sale_id: int) -> SalesData | None:
        stmt: Select[tuple[SalesData]] = select(SalesData).where(
            SalesData.id == sale_id
        )
        return self.db.scalar(stmt)

    def get_all(self) -> list[SalesData]:
        stmt: Select[tuple[SalesData]] = select(SalesData)
        return list(self.db.scalars(stmt).all())

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

    def delete(self, sale_id: int) -> None:
        stmt = delete(SalesData).where(SalesData.id == sale_id)
        self.db.execute(stmt)
        self.db.commit()
