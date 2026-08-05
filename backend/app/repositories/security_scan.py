from datetime import date

from sqlalchemy import (
    Select,
    case,
    desc,
    func,
    select,
)
from sqlalchemy.orm import Session

from app.models.security_scan import SecurityScan


class SecurityScanRepository:
    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def _apply_filters(
        self,
        stmt: Select,
        start_date: date | None = None,
        end_date: date | None = None,
        risk_level: str | None = None,
        status: str | None = None,
        threat_type: str | None = None,
    ) -> Select:
        if start_date:
            stmt = stmt.where(
                SecurityScan.created_at >= start_date,
            )

        if end_date:
            stmt = stmt.where(
                SecurityScan.created_at <= end_date,
            )

        if risk_level:
            stmt = stmt.where(
                SecurityScan.risk_level == risk_level,
            )

        if status:
            stmt = stmt.where(
                SecurityScan.status == status,
            )

        if threat_type:
            stmt = stmt.where(
                SecurityScan.threat_type == threat_type,
            )

        return stmt

    def get_scan_by_id(
        self,
        scan_id: int,
    ):
        stmt = select(
            SecurityScan,
        ).where(
            SecurityScan.id == scan_id,
        )

        return self.db.execute(
            stmt,
        ).scalar_one_or_none()

    def get_latest_scan(
        self,
    ):
        stmt = (
            select(
                SecurityScan,
            )
            .order_by(
                desc(
                    SecurityScan.created_at,
                )
            )
            .limit(1)
        )

        return self.db.execute(
            stmt,
        ).scalar_one_or_none()

    def create_scan(
        self,
        scan: SecurityScan,
    ) -> SecurityScan:
        self.db.add(scan)
        self.db.commit()
        self.db.refresh(scan)

        return scan

    def list_scans(
        self,
        page: int = 1,
        limit: int = 20,
        start_date: date | None = None,
        end_date: date | None = None,
        risk_level: str | None = None,
        status: str | None = None,
        threat_type: str | None = None,
    ):
        stmt = select(SecurityScan)

        stmt = self._apply_filters(
            stmt,
            start_date,
            end_date,
            risk_level,
            status,
            threat_type,
        )

        stmt = (
            stmt.order_by(
                desc(SecurityScan.created_at),
            )
            .offset((page - 1) * limit)
            .limit(limit)
        )

        return self.db.execute(stmt).scalars().all()

    def update_scan(
        self,
        scan: SecurityScan,
    ) -> SecurityScan:
        self.db.commit()
        self.db.refresh(scan)

        return scan

    def delete_scan(
        self,
        scan: SecurityScan,
    ) -> None:
        self.db.delete(scan)
        self.db.commit()

    def count_scans(
        self,
        start_date: date | None = None,
        end_date: date | None = None,
        risk_level: str | None = None,
        status: str | None = None,
        threat_type: str | None = None,
    ) -> int:
        stmt = select(
            func.count(SecurityScan.id),
        )

        stmt = self._apply_filters(
            stmt,
            start_date,
            end_date,
            risk_level,
            status,
            threat_type,
        )

        return self.db.execute(stmt).scalar_one()

    def count_by_risk(
        self,
    ):
        stmt = (
            select(
                SecurityScan.risk_level,
                func.count(SecurityScan.id).label("total"),
            )
            .group_by(SecurityScan.risk_level)
            .order_by(SecurityScan.risk_level)
        )

        return self.db.execute(stmt).all()

    def count_by_status(
        self,
    ):
        stmt = (
            select(
                SecurityScan.status,
                func.count(SecurityScan.id).label("total"),
            )
            .group_by(SecurityScan.status)
            .order_by(SecurityScan.status)
        )

        return self.db.execute(stmt).all()

    def average_security_score(
        self,
    ):
        stmt = select(
            func.coalesce(
                func.avg(SecurityScan.security_score),
                0,
            )
        )

        return self.db.execute(stmt).scalar_one()

    def duplicate_file_count(
        self,
    ):
        stmt = select(
            func.count(SecurityScan.id),
        ).where(
            SecurityScan.is_duplicate.is_(True),
        )

        return self.db.execute(stmt).scalar_one()

    def get_scan_by_upload_id(
        self,
        upload_id: int,
    ):
        stmt = (
            select(SecurityScan)
            .where(
                SecurityScan.upload_id == upload_id,
            )
            .order_by(
                desc(SecurityScan.created_at),
            )
        )

        return self.db.execute(stmt).scalars().all()

    def security_summary(
        self,
        start_date: date | None = None,
        end_date: date | None = None,
        risk_level: str | None = None,
        status: str | None = None,
        threat_type: str | None = None,
    ):
        stmt = select(
            func.count(
                SecurityScan.id,
            ).label("total_scans"),
            func.coalesce(
                func.avg(
                    SecurityScan.security_score,
                ),
                0,
            ).label("average_score"),
            func.coalesce(
                func.sum(
                    case(
                        (
                            SecurityScan.is_duplicate.is_(True),
                            1,
                        ),
                        else_=0,
                    )
                ),
                0,
            ).label("duplicate_files"),
        )

        stmt = self._apply_filters(
            stmt,
            start_date,
            end_date,
            risk_level,
            status,
            threat_type,
        )

        return self.db.execute(
            stmt,
        ).one()
