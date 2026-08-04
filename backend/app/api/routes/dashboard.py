from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.dashboard import DashboardRepository
from app.schemas.dashboard import DashboardSummaryResponse
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
    service: DashboardService = Depends(get_dashboard_service),
):
    return service.get_summary()
