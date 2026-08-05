from datetime import date

from fastapi import (
    APIRouter,
    Depends,
    Query,
)
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.dashboard import DashboardRepository
from app.schemas.dashboard import (
    DashboardCategoryResponse,
    DashboardMonthlyResponse,
    DashboardRegionResponse,
    DashboardSummaryResponse,
    DashboardTopProductResponse,
)
from app.services.dashboard import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


def get_dashboard_service(
    db: Session = Depends(get_db),
) -> DashboardService:
    repository = DashboardRepository(db)
    return DashboardService(repository)


@router.get(
    "/summary",
    response_model=DashboardSummaryResponse,
    summary="Get dashboard summary",
    description="Retrieve overall sales statistics.",
    response_description="Dashboard summary.",
)
def get_dashboard_summary(
    start_date: date | None = Query(
        default=None,
        description="Filter by start date.",
    ),
    end_date: date | None = Query(
        default=None,
        description="Filter by end date.",
    ),
    category: str | None = Query(
        default=None,
        description="Filter by category.",
    ),
    region: str | None = Query(
        default=None,
        description="Filter by region.",
    ),
    service: DashboardService = Depends(
        get_dashboard_service,
    ),
):
    return service.get_summary(
        start_date,
        end_date,
        category,
        region,
    )


@router.get(
    "/category",
    response_model=list[DashboardCategoryResponse],
    summary="Revenue by category",
    description="Retrieve sales grouped by category.",
)
def get_revenue_by_category(
    start_date: date | None = Query(
        default=None,
        description="Filter by start date.",
    ),
    end_date: date | None = Query(
        default=None,
        description="Filter by end date.",
    ),
    category: str | None = Query(
        default=None,
        description="Filter by category.",
    ),
    region: str | None = Query(
        default=None,
        description="Filter by region.",
    ),
    service: DashboardService = Depends(
        get_dashboard_service,
    ),
):
    return service.get_revenue_by_category(
        start_date,
        end_date,
        category,
        region,
    )


@router.get(
    "/region",
    response_model=list[DashboardRegionResponse],
    summary="Revenue by region",
    description="Retrieve sales grouped by region.",
)
def get_revenue_by_region(
    start_date: date | None = Query(
        default=None,
        description="Filter by start date.",
    ),
    end_date: date | None = Query(
        default=None,
        description="Filter by end date.",
    ),
    category: str | None = Query(
        default=None,
        description="Filter by category.",
    ),
    region: str | None = Query(
        default=None,
        description="Filter by region.",
    ),
    service: DashboardService = Depends(
        get_dashboard_service,
    ),
):
    return service.get_revenue_by_region(
        start_date,
        end_date,
        category,
        region,
    )


@router.get(
    "/monthly",
    response_model=list[DashboardMonthlyResponse],
    summary="Monthly revenue",
    description="Retrieve monthly revenue statistics.",
)
def get_monthly_revenue(
    start_date: date | None = Query(
        default=None,
        description="Filter by start date.",
    ),
    end_date: date | None = Query(
        default=None,
        description="Filter by end date.",
    ),
    category: str | None = Query(
        default=None,
        description="Filter by category.",
    ),
    region: str | None = Query(
        default=None,
        description="Filter by region.",
    ),
    service: DashboardService = Depends(
        get_dashboard_service,
    ),
):
    return service.get_monthly_revenue(
        start_date,
        end_date,
        category,
        region,
    )


@router.get(
    "/top-products",
    response_model=list[DashboardTopProductResponse],
    summary="Top selling products",
    description="Retrieve top selling products by quantity.",
)
def get_top_products(
    start_date: date | None = Query(default=None),
    end_date: date | None = Query(default=None),
    category: str | None = Query(default=None),
    region: str | None = Query(default=None),
    limit: int = Query(
        default=10,
        ge=1,
        le=100,
    ),
    service: DashboardService = Depends(
        get_dashboard_service,
    ),
):
    return service.get_top_products(
        start_date,
        end_date,
        category,
        region,
        limit,
    )
