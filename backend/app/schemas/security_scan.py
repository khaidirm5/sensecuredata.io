from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class SecurityScanCreate(BaseModel):
    upload_id: int
    filename: str
    file_hash: str
    mime_type: str
    extension: str
    file_size: int
    is_duplicate: bool = False
    risk_level: str
    security_score: int
    status: str
    threat_type: str = "NONE"
    scan_duration_ms: int = 0
    scanner_version: str = "v1.0"
    scan_details: dict[str, Any] | None = None


class SecurityScanUpdate(BaseModel):
    risk_level: str | None = None
    security_score: int | None = None
    status: str | None = None
    threat_type: str | None = None
    scan_duration_ms: int | None = None
    scanner_version: str | None = None
    scan_details: dict[str, Any] | None = None


class SecurityScanResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    upload_id: int
    filename: str
    file_hash: str
    mime_type: str
    extension: str
    file_size: int
    is_duplicate: bool
    risk_level: str
    security_score: int
    status: str
    threat_type: str
    scan_duration_ms: int
    scanner_version: str
    scan_details: dict[str, Any] | None
    created_at: datetime


class SecurityScanListResponse(BaseModel):
    items: list[SecurityScanResponse]
    total: int
    page: int
    limit: int


class SecurityScanSummaryResponse(BaseModel):
    total_scans: int
    average_score: float
    duplicate_files: int


class RiskDistributionResponse(BaseModel):
    risk_level: str
    total: int


class StatusDistributionResponse(BaseModel):
    status: str
    total: int
