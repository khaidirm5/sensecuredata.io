from datetime import datetime

from pydantic import BaseModel


class UploadSummary(BaseModel):
    total_rows: int
    valid_rows: int
    invalid_rows: int
    duplicate_rows: int


class UploadResponse(BaseModel):
    message: str
    upload_id: int
    filename: str
    file_type: str
    status: str
    uploaded_at: datetime
    summary: UploadSummary
