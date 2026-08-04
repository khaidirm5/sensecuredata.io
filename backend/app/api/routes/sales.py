from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.sales import SalesRepository
from app.schemas.sales import (
    SalesCreate,
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
    summary="Create a new sales record",
    description="Create a new sales record and store it in the database.",
    response_model=SalesResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_sale(
    data: SalesCreate,
    service: SalesService = Depends(get_sales_service),
):
    return service.create_sale(data)


@router.get(
    "/",
    summary="List sales records",
    description="Retrieve all sales records from the database.",
    response_model=list[SalesResponse],
)
def get_sales(
    service: SalesService = Depends(get_sales_service),
):
    return service.get_sales()


@router.get(
    "/{sale_id}",
    summary="Get a sales record by ID",
    description="Retrieve a single sales record using its unique ID.",
    response_model=SalesResponse,
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
    summary="Update a sales record",
    description="Update an existing sales record by its ID.",
    response_model=SalesResponse,
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
    summary="Delete a sales record",
    description="Delete an existing sales record by its ID.",
    status_code=status.HTTP_204_NO_CONTENT,
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
