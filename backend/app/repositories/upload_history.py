from sqlalchemy import Select, func, select
from sqlalchemy.orm import Session

from app.models.upload_history import UploadHistory


class UploadHistoryRepository:
    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        upload: UploadHistory,
    ) -> UploadHistory:
        self.db.add(upload)
        self.db.commit()
        self.db.refresh(upload)

        return upload

    def get_by_id(
        self,
        upload_id: int,
    ) -> UploadHistory | None:
        stmt: Select[tuple[UploadHistory]] = select(UploadHistory).where(
            UploadHistory.id == upload_id
        )

        return self.db.scalar(stmt)

    def update(
        self,
        upload: UploadHistory,
    ) -> UploadHistory:
        self.db.commit()
        self.db.refresh(upload)

        return upload

    def get_all(
        self,
        skip: int = 0,
        limit: int = 20,
    ) -> list[UploadHistory]:
        stmt: Select[tuple[UploadHistory]] = (
            select(UploadHistory)
            .order_by(UploadHistory.uploaded_at.desc())
            .offset(skip)
            .limit(limit)
        )

        return list(self.db.scalars(stmt).all())

    def count(self) -> int:
        stmt = select(func.count()).select_from(UploadHistory)
        return self.db.scalar(stmt) or 0

    def delete(
        self,
        upload: UploadHistory,
    ) -> None:
        self.db.delete(upload)
        self.db.commit()

    def get_latest(
        self,
        limit: int = 10,
    ) -> list[UploadHistory]:
        stmt: Select[tuple[UploadHistory]] = (
            select(UploadHistory)
            .order_by(UploadHistory.uploaded_at.desc())
            .limit(limit)
        )

        return list(self.db.scalars(stmt).all())
