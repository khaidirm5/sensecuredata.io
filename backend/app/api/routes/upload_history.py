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
from app.repositories.upload_history import UploadHistoryRepository
from app.schemas.upload_history import (
    UploadHistoryListResponse,
    UploadHistoryResponse,
)
from app.services.upload_history import UploadHistoryService

router = APIRouter(
    prefix="/upload-history",
    tags=["Upload History"],
)


def get_upload_history_service(
    db: Session = Depends(get_db),
) -> UploadHistoryService:
    repository = UploadHistoryRepository(db)

    return UploadHistoryService(repository)


@router.get(
    "/",
    response_model=UploadHistoryListResponse,
    summary="Get upload history",
)
def get_upload_history(
    page: int = Query(
        default=1,
        ge=1,
    ),
    limit: int = Query(
        default=20,
        ge=1,
        le=100,
    ),
    service: UploadHistoryService = Depends(
        get_upload_history_service,
    ),
):
    return service.list_uploads(
        page=page,
        limit=limit,
    )


@router.get(
    "/latest",
    response_model=list[UploadHistoryResponse],
    summary="Get latest upload history",
)
def get_latest_uploads(
    limit: int = Query(
        default=10,
        ge=1,
        le=100,
    ),
    service: UploadHistoryService = Depends(
        get_upload_history_service,
    ),
):
    return service.get_latest_uploads(
        limit=limit,
    )


@router.get(
    "/{upload_id}",
    response_model=UploadHistoryResponse,
    summary="Get upload history by ID",
)
def get_upload(
    upload_id: int,
    service: UploadHistoryService = Depends(
        get_upload_history_service,
    ),
):
    try:
        return service.get_upload(
            upload_id,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.delete(
    "/{upload_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete upload history",
)
def delete_upload(
    upload_id: int,
    service: UploadHistoryService = Depends(
        get_upload_history_service,
    ),
):
    try:
        service.delete_upload(
            upload_id,
        )

        return Response(
            status_code=status.HTTP_204_NO_CONTENT,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
