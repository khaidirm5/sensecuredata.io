from app.models.sales_data import SalesData
from app.repositories.sales import SalesRepository
from app.schemas.sales import SalesCreate, SalesUpdate


class SalesService:
    def __init__(self, repository: SalesRepository):
        self.repository = repository

    def create_sale(self, data: SalesCreate) -> SalesData:
        return self.repository.create(data)

    def get_sale(self, sale_id: int) -> SalesData | None:
        return self.repository.get_by_id(sale_id)

    def get_sales(self) -> list[SalesData]:
        return self.repository.get_all()

    def update_sale(
        self,
        sale_id: int,
        data: SalesUpdate,
    ) -> SalesData | None:
        sale = self.repository.get_by_id(sale_id)

        if sale is None:
            return None

        return self.repository.update(sale, data)

    def delete_sale(self, sale_id: int) -> bool:
        sale = self.repository.get_by_id(sale_id)

        if sale is None:
            return False

        self.repository.delete(sale_id)
        return True
