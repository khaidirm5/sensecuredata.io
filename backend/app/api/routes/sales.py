from typing import Literal

from fastapi import (
    APIRouter,
    Depends,
    File,
    HTTPException,
    Query,
    Response,
    UploadFile,
    status,
)
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, require_roles
from app.db.session import get_db
from app.models.user import User
from app.repositories.sales import SalesRepository
from app.repositories.security_scan import SecurityScanRepository
from app.repositories.upload_history import UploadHistoryRepository
from app.schemas.sales import (
    SalesCreate,
    SalesListResponse,
    SalesResponse,
    SalesUpdate,
)
from app.schemas.security_scan import SecurityScanCreate
from app.schemas.upload import UploadResponse, UploadSummary
from app.services.etl import ETLService
from app.services.sales import SalesService
from app.services.security_scan import SecurityScanService
from app.services.upload_history import UploadHistoryService
from app.utils.etl.exceptions import (
    ETLLoadError,
    ETLReaderError,
    ETLTransformationError,
    ETLValidationError,
)
from app.utils.file_storage import FileStorage
from app.utils.file_validator import FileValidator
from app.utils.security.security_engine import SecurityEngine

router = APIRouter(
    prefix="/sales",
    tags=["Sales"],
)


def get_sales_service(
    db: Session = Depends(get_db),
) -> SalesService:
    repository = SalesRepository(db)
    return SalesService(repository)


def get_upload_history_service(
    db: Session = Depends(get_db),
) -> UploadHistoryService:
    repository = UploadHistoryRepository(db)
    return UploadHistoryService(repository)


def get_security_scan_service(
    db: Session = Depends(get_db),
) -> SecurityScanService:
    repository = SecurityScanRepository(db)
    return SecurityScanService(repository)


def get_etl_service(
    db: Session = Depends(get_db),
) -> ETLService:
    return ETLService(db)


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
    _: User = Depends(
        require_roles(
            "admin",
            "analyst",
        ),
    ),
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
    _: User = Depends(get_current_user),
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


@router.post(
    "/upload",
    response_model=UploadResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Upload sales data",
    description=(
        "Upload CSV or Excel sales data and process it through the ETL pipeline."
    ),
)
async def upload_sales(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    upload_service: UploadHistoryService = Depends(
        get_upload_history_service,
    ),
    security_service: SecurityScanService = Depends(
        get_security_scan_service,
    ),
    etl_service: ETLService = Depends(
        get_etl_service,
    ),
):
    file_path = None
    upload = None
    try:
        file_type = FileValidator.validate(file)

        file_path = await FileStorage.save(file)

        upload = upload_service.create_upload(
            uploaded_by=current_user.id,
            filename=file.filename,
            file_type=file_type,
        )

        security_engine = SecurityEngine(
            etl_service.db,
        )

        scan_result = security_engine.scan(
            file_path,
        )

        security_service.create_scan(
            SecurityScanCreate(
                upload_id=upload.id,
                **scan_result,
            )
        )

        result = etl_service.process_file(
            file_path=file_path,
            upload_id=upload.id,
        )

        upload = upload_service.mark_success(
            upload,
            total_rows=result.total_rows,
            valid_rows=result.valid_rows,
            invalid_rows=result.invalid_rows,
        )

        return UploadResponse(
            message="Sales data uploaded successfully.",
            upload_id=upload.id,
            filename=upload.filename,
            file_type=upload.file_type,
            status=upload.status,
            uploaded_at=upload.uploaded_at,
            summary=UploadSummary(
                total_rows=result.total_rows,
                valid_rows=result.valid_rows,
                invalid_rows=result.invalid_rows,
                duplicate_rows=result.duplicate_rows,
            ),
        )

    except (
        ETLReaderError,
        ETLValidationError,
        ETLTransformationError,
        ETLLoadError,
    ) as exc:
        if upload is not None:
            upload_service.mark_failed(
                upload,
                str(exc),
            )

    except ValueError as exc:
        if upload is not None:
            upload_service.mark_failed(
                upload,
                str(exc),
            )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )

    except Exception as exc:
        if upload is not None:
            upload_service.mark_failed(
                upload,
                str(exc),
            )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected server error.",
        ) from exc
    finally:
        if file_path is not None:
            FileStorage.delete(file_path)


@router.get(
    "/{sale_id}",
    response_model=SalesResponse,
    summary="Get a sales record by ID",
    description="Retrieve a single sales record by its ID.",
    response_description="Sales record.",
)
def get_sale(
    sale_id: int,
    _: User = Depends(get_current_user),
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
    _: User = Depends(
        require_roles(
            "admin",
            "analyst",
        ),
    ),
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
    _: User = Depends(
        require_roles(
            "admin",
        ),
    ),
    service: SalesService = Depends(get_sales_service),
):
    deleted = service.delete_sale(sale_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sale not found",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
