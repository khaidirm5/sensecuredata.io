from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UploadResponse(BaseModel):
    id: int
    filename: str
    file_type: str
    total_rows: int
    valid_rows: int
    invalid_rows: int
    status: str
    error_message: str | None
    uploaded_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )
