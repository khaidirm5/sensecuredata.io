from pathlib import Path

from fastapi import UploadFile


class FileValidator:
    """Validate uploaded files."""

    ALLOWED_EXTENSIONS = {
        ".csv",
        ".xlsx",
    }

    @classmethod
    def validate(
        cls,
        file: UploadFile,
    ) -> str:
        if not file.filename:
            raise ValueError("Filename is required.")

        extension = Path(file.filename).suffix.lower()

        if extension not in cls.ALLOWED_EXTENSIONS:
            raise ValueError("Only CSV (.csv) and Excel (.xlsx) files are supported.")

        return extension.removeprefix(".")
