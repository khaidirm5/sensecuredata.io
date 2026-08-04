from typing import Literal

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    Response,
    status,
)
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.sales import SalesRepository
from app.schemas.sales import (
    SalesCreate,
    SalesListResponse,
    SalesResponse,
    SalesUpdate,
)
from app.services.sales import SalesService

router = APIRouter(
    prefix="/sales",
    tags=["Sales"],
)


def get_sales_service(
    db: Session = Depends(get_db),
) -> SalesService:
    repository = SalesRepository(db)
    return SalesService(repository)


@router.post(
    "/",
    response_model=SalesResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new sales record",
    description="Create a new sales record in the database.",
    response_description="Created sales record.",
)
def create_sale(
    data: SalesCreate,
    service: SalesService = Depends(get_sales_service),
):
    return service.create_sale(data)


@router.get(
    "/",
    response_model=SalesListResponse,
    summary="Get sales records",
    description=(
        "Retrieve sales records with pagination, search, filtering, and sorting."
    ),
    response_description="Paginated sales records.",
)
def get_sales(
    page: int = Query(
        default=1,
        ge=1,
        description="Page number.",
    ),
    limit: int = Query(
        default=20,
        ge=1,
        le=100,
        description="Number of records per page.",
    ),
    search: str | None = Query(
        default=None,
        description="Search by invoice number, product name, category, or region.",
    ),
    category: str | None = Query(
        default=None,
        description="Filter by category.",
    ),
    region: str | None = Query(
        default=None,
        description="Filter by region.",
    ),
    sort_by: str = Query(
        default="order_date",
        description="Field used for sorting.",
    ),
    order: Literal["asc", "desc"] = Query(
        default="desc",
        description="Sort direction.",
    ),
    service: SalesService = Depends(get_sales_service),
):
    return service.get_sales(
        page=page,
        limit=limit,
        search=search,
        category=category,
        region=region,
        sort_by=sort_by,
        order=order,
    )


@router.get(
    "/{sale_id}",
    response_model=SalesResponse,
    summary="Get a sales record by ID",
    description="Retrieve a single sales record by its ID.",
    response_description="Sales record.",
)
def get_sale(
    sale_id: int,
    service: SalesService = Depends(get_sales_service),
):
    sale = service.get_sale(sale_id)

    if sale is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sale not found",
        )

    return sale


@router.put(
    "/{sale_id}",
    response_model=SalesResponse,
    summary="Update a sales record",
    description="Update an existing sales record.",
    response_description="Updated sales record.",
)
def update_sale(
    sale_id: int,
    data: SalesUpdate,
    service: SalesService = Depends(get_sales_service),
):
    sale = service.update_sale(
        sale_id,
        data,
    )

    if sale is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sale not found",
        )

    return sale


@router.delete(
    "/{sale_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a sales record",
    description="Delete a sales record by its ID.",
)
def delete_sale(
    sale_id: int,
    service: SalesService = Depends(get_sales_service),
):
    deleted = service.delete_sale(sale_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sale not found",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
