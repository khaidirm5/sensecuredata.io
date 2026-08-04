from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile


class FileStorage:
    """Utility for storing uploaded files."""

    UPLOAD_DIR = Path("uploads")

    @classmethod
    async def save(
        cls,
        file: UploadFile,
    ) -> Path:
        cls.UPLOAD_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        filename = f"{uuid4().hex}_{file.filename}"

        destination = cls.UPLOAD_DIR / filename

        content = await file.read()

        destination.write_bytes(content)

        return destination

    @staticmethod
    def delete(
        file_path: str,
    ) -> None:
        Path(file_path).unlink(
            missing_ok=True,
        )
