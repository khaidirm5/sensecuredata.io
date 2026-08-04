from app.models.upload_history import UploadHistory
from app.repositories.upload_history import UploadHistoryRepository


class UploadHistoryService:
    def __init__(
        self,
        repository: UploadHistoryRepository,
    ):
        self.repository = repository

    def create_upload(
        self,
        *,
        uploaded_by: int,
        filename: str,
        file_type: str,
    ) -> UploadHistory:
        upload = UploadHistory(
            uploaded_by=uploaded_by,
            filename=filename,
            file_type=file_type,
            total_rows=0,
            valid_rows=0,
            invalid_rows=0,
            status="PROCESSING",
            error_message=None,
        )

        return self.repository.create(upload)

    def mark_success(
        self,
        upload: UploadHistory,
        *,
        total_rows: int,
        valid_rows: int,
        invalid_rows: int = 0,
    ) -> UploadHistory:
        upload.total_rows = total_rows
        upload.valid_rows = valid_rows
        upload.invalid_rows = invalid_rows
        upload.status = "SUCCESS"
        upload.error_message = None

        return self.repository.update(upload)

    def mark_failed(
        self,
        upload: UploadHistory,
        error_message: str,
    ) -> UploadHistory:
        upload.status = "FAILED"
        upload.error_message = error_message

        return self.repository.update(upload)
