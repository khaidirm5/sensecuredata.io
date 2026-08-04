from sqlalchemy import Select, select
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
