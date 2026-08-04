from math import ceil

from app.models.sales_data import SalesData
from app.repositories.sales import SalesRepository
from app.schemas.sales import (
    Pagination,
    SalesCreate,
    SalesListResponse,
    SalesUpdate,
)


class SalesService:
    ALLOWED_SORT_FIELDS = {
        "invoice_number",
        "order_date",
        "product_name",
        "category",
        "quantity",
        "unit_price",
        "total_price",
        "region",
        "created_at",
    }

    ALLOWED_ORDER = {
        "asc",
        "desc",
    }

    DEFAULT_LIMIT = 20
    MAX_LIMIT = 100

    def __init__(self, repository: SalesRepository):
        self.repository = repository

    def create_sale(
        self,
        data: SalesCreate,
    ) -> SalesData:
        return self.repository.create(data)

    def get_sale(
        self,
        sale_id: int,
    ) -> SalesData | None:
        return self.repository.get_by_id(sale_id)

    def get_sales(
        self,
        *,
        page: int = 1,
        limit: int = DEFAULT_LIMIT,
        search: str | None = None,
        category: str | None = None,
        region: str | None = None,
        sort_by: str = "order_date",
        order: str = "desc",
    ) -> SalesListResponse:

        if page < 1:
            page = 1

        if limit < 1:
            limit = self.DEFAULT_LIMIT

        if limit > self.MAX_LIMIT:
            limit = self.MAX_LIMIT

        search = search.strip() if search else None
        category = category.strip() if category else None
        region = region.strip() if region else None

        if sort_by not in self.ALLOWED_SORT_FIELDS:
            sort_by = "order_date"

        order = order.lower()

        if order not in self.ALLOWED_ORDER:
            order = "desc"

        skip = (page - 1) * limit

        items = self.repository.get_all(
            skip=skip,
            limit=limit,
            search=search,
            category=category,
            region=region,
            sort_by=sort_by,
            order=order,
        )

        total = self.repository.count(
            search=search,
            category=category,
            region=region,
        )

        total_pages = ceil(total / limit) if total else 1

        return SalesListResponse(
            items=items,
            pagination=Pagination(
                page=page,
                limit=limit,
                total=total,
                total_pages=total_pages,
                has_next=page < total_pages,
                has_previous=page > 1,
            ),
        )

    def update_sale(
        self,
        sale_id: int,
        data: SalesUpdate,
    ) -> SalesData | None:
        sale = self.repository.get_by_id(sale_id)

        if sale is None:
            return None

        return self.repository.update(
            sale,
            data,
        )

    def delete_sale(
        self,
        sale_id: int,
    ) -> bool:
        sale = self.repository.get_by_id(sale_id)

        if sale is None:
            return False

        self.repository.delete(sale_id)

        return True
