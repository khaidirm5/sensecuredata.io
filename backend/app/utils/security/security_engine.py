import mimetypes
from pathlib import Path

from sqlalchemy.orm import Session

from app.utils.security.duplicate_detector import DuplicateDetector
from app.utils.security.file_hash import FileHash
from app.utils.security.risk_analyzer import RiskAnalyzer


class SecurityEngine:
    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def scan(
        self,
        file_path: str | Path,
    ) -> dict:
        file = Path(file_path)

        file_hash = FileHash.generate(file)

        is_duplicate = DuplicateDetector.is_duplicate(
            self.db,
            file_hash,
        )

        mime_type = mimetypes.guess_type(file.name)[0] or "application/octet-stream"

        analysis = RiskAnalyzer.analyze(
            file,
            is_duplicate=is_duplicate,
        )

        return {
            "filename": file.name,
            "file_hash": file_hash,
            "mime_type": mime_type,
            "extension": file.suffix.lower(),
            "file_size": file.stat().st_size,
            "is_duplicate": is_duplicate,
            "status": "COMPLETED",
            "scan_duration_ms": 0,
            "scanner_version": "v1.0",
            **analysis,
        }
