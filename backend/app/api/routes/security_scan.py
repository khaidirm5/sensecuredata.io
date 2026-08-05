from datetime import date

from fastapi import (
    APIRouter,
    Depends,
    Query,
)
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.security_scan import SecurityScanRepository
from app.schemas.security_scan import (
    RiskDistributionResponse,
    SecurityScanCreate,
    SecurityScanListResponse,
    SecurityScanResponse,
    SecurityScanSummaryResponse,
    SecurityScanUpdate,
    StatusDistributionResponse,
)
from app.services.security_scan import SecurityScanService

router = APIRouter(
    prefix="/security-scans",
    tags=["Security Scans"],
)


def get_security_scan_service(
    db: Session = Depends(get_db),
) -> SecurityScanService:
    repository = SecurityScanRepository(db)
    return SecurityScanService(repository)


@router.get(
    "",
    response_model=SecurityScanListResponse,
    summary="List security scans",
)
def list_security_scans(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=20, ge=1, le=100),
    start_date: date | None = Query(default=None),
    end_date: date | None = Query(default=None),
    risk_level: str | None = Query(default=None),
    status: str | None = Query(default=None),
    threat_type: str | None = Query(default=None),
    service: SecurityScanService = Depends(
        get_security_scan_service,
    ),
):
    return service.list_scans(
        page,
        limit,
        start_date,
        end_date,
        risk_level,
        status,
        threat_type,
    )


@router.get(
    "/summary",
    response_model=SecurityScanSummaryResponse,
)
def get_security_summary(
    db: Session = Depends(get_db),
):
    repository = SecurityScanRepository(db)
    service = SecurityScanService(repository)

    return service.security_summary()


@router.get(
    "/risk-distribution",
    response_model=list[RiskDistributionResponse],
    summary="Risk level distribution",
)
def get_risk_distribution(
    service: SecurityScanService = Depends(
        get_security_scan_service,
    ),
):
    return service.count_by_risk()


@router.get(
    "/status-distribution",
    response_model=list[StatusDistributionResponse],
    summary="Status distribution",
)
def get_status_distribution(
    service: SecurityScanService = Depends(
        get_security_scan_service,
    ),
):
    return service.count_by_status()


@router.get(
    "/latest",
    response_model=SecurityScanResponse,
    summary="Latest security scan",
)
def get_latest_scan(
    service: SecurityScanService = Depends(
        get_security_scan_service,
    ),
):
    return service.get_latest_scan()


@router.get(
    "/upload/{upload_id}",
    response_model=list[SecurityScanResponse],
    summary="Scans by upload",
)
def get_scans_by_upload(
    upload_id: int,
    service: SecurityScanService = Depends(
        get_security_scan_service,
    ),
):
    return service.get_scan_by_upload_id(upload_id)


@router.get(
    "/{scan_id}",
    response_model=SecurityScanResponse,
    summary="Scan detail",
)
def get_scan(
    scan_id: int,
    service: SecurityScanService = Depends(
        get_security_scan_service,
    ),
):
    return service.get_scan_by_id(scan_id)


@router.post(
    "",
    response_model=SecurityScanResponse,
    summary="Create security scan",
)
def create_security_scan(
    data: SecurityScanCreate,
    service: SecurityScanService = Depends(
        get_security_scan_service,
    ),
):
    return service.create_scan(data)


@router.put(
    "/{scan_id}",
    response_model=SecurityScanResponse,
    summary="Update security scan",
)
def update_security_scan(
    scan_id: int,
    data: SecurityScanUpdate,
    service: SecurityScanService = Depends(
        get_security_scan_service,
    ),
):
    return service.update_scan(
        scan_id,
        data,
    )


@router.delete(
    "/{scan_id}",
    summary="Delete security scan",
)
def delete_security_scan(
    scan_id: int,
    service: SecurityScanService = Depends(
        get_security_scan_service,
    ),
):
    service.delete_scan(scan_id)

    return {"message": "Security scan deleted successfully."}
