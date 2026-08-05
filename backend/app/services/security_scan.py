from datetime import date
from decimal import Decimal

from app.models.security_scan import SecurityScan
from app.repositories.security_scan import SecurityScanRepository
from app.schemas.security_scan import (
    SecurityScanCreate,
    SecurityScanListResponse,
    SecurityScanResponse,
    SecurityScanSummaryResponse,
    SecurityScanUpdate,
)


class SecurityScanService:
    def __init__(
        self,
        repository: SecurityScanRepository,
    ):
        self.repository = repository

    def create_scan(
        self,
        data: SecurityScanCreate,
    ) -> SecurityScanResponse:
        scan = SecurityScan(
            **data.model_dump(),
        )

        scan = self.repository.create_scan(scan)

        return SecurityScanResponse.model_validate(
            scan,
        )

    def get_scan_by_id(
        self,
        scan_id: int,
    ) -> SecurityScanResponse:
        scan = self.repository.get_scan_by_id(
            scan_id,
        )

        if scan is None:
            raise ValueError(
                "Security scan not found.",
            )

        return SecurityScanResponse.model_validate(
            scan,
        )

    def get_latest_scan(
        self,
    ) -> SecurityScanResponse:
        scan = self.repository.get_latest_scan()

        if scan is None:
            raise ValueError(
                "No security scans found.",
            )

        return SecurityScanResponse.model_validate(
            scan,
        )

    def list_scans(
        self,
        page: int = 1,
        limit: int = 20,
        start_date: date | None = None,
        end_date: date | None = None,
        risk_level: str | None = None,
        status: str | None = None,
        threat_type: str | None = None,
    ) -> SecurityScanListResponse:
        scans = self.repository.list_scans(
            page,
            limit,
            start_date,
            end_date,
            risk_level,
            status,
            threat_type,
        )

        total = self.repository.count_scans(
            start_date,
            end_date,
            risk_level,
            status,
            threat_type,
        )

        return SecurityScanListResponse(
            total=total,
            page=page,
            limit=limit,
            items=[
                SecurityScanResponse.model_validate(
                    scan,
                )
                for scan in scans
            ],
        )

    def update_scan(
        self,
        scan_id: int,
        data: SecurityScanUpdate,
    ) -> SecurityScanResponse:
        scan = self.repository.get_scan_by_id(
            scan_id,
        )

        if scan is None:
            raise ValueError(
                "Security scan not found.",
            )

        for key, value in data.model_dump(
            exclude_unset=True,
        ).items():
            setattr(
                scan,
                key,
                value,
            )

        scan = self.repository.update_scan(
            scan,
        )

        return SecurityScanResponse.model_validate(
            scan,
        )

    def delete_scan(
        self,
        scan_id: int,
    ) -> None:
        scan = self.repository.get_scan_by_id(
            scan_id,
        )

        if scan is None:
            raise ValueError(
                "Security scan not found.",
            )

        self.repository.delete_scan(
            scan,
        )

    def get_scan_by_upload_id(
        self,
        upload_id: int,
    ) -> list[SecurityScanResponse]:
        scans = self.repository.get_scan_by_upload_id(
            upload_id,
        )

        return [
            SecurityScanResponse.model_validate(
                scan,
            )
            for scan in scans
        ]

    def security_summary(
        self,
        start_date: date | None = None,
        end_date: date | None = None,
        risk_level: str | None = None,
        status: str | None = None,
        threat_type: str | None = None,
    ) -> SecurityScanSummaryResponse:
        summary = self.repository.security_summary(
            start_date,
            end_date,
            risk_level,
            status,
            threat_type,
        )

        average_score = Decimal(
            str(summary.average_score),
        ).quantize(
            Decimal("0.01"),
        )

        return SecurityScanSummaryResponse(
            total_scans=summary.total_scans,
            average_score=float(average_score),
            duplicate_files=summary.duplicate_files,
        )

    def count_by_risk(
        self,
    ) -> list[dict]:
        rows = self.repository.count_by_risk()

        return [
            {
                "risk_level": row.risk_level,
                "total": row.total,
            }
            for row in rows
        ]

    def count_by_status(
        self,
    ) -> list[dict]:
        rows = self.repository.count_by_status()

        return [
            {
                "status": row.status,
                "total": row.total,
            }
            for row in rows
        ]

    def average_security_score(
        self,
    ) -> Decimal:
        score = self.repository.average_security_score()

        if isinstance(
            score,
            Decimal,
        ):
            return score.quantize(
                Decimal("0.01"),
            )

        return Decimal(
            str(score),
        ).quantize(
            Decimal("0.01"),
        )

    def duplicate_file_count(
        self,
    ) -> int:
        return self.repository.duplicate_file_count()
