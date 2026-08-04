from pathlib import Path

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.models.sales_data import SalesData
from app.schemas.etl import ETLResult
from app.utils.etl.cleaner import DataCleaner
from app.utils.etl.exceptions import (
    ETLLoadError,
    ETLReaderError,
    ETLTransformationError,
    ETLValidationError,
)
from app.utils.etl.loader import DataLoader
from app.utils.etl.reader import FileReader
from app.utils.etl.transformer import DataTransformer
from app.utils.etl.validator import DataValidator


class ETLService:
    """Sales ETL Service."""

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def process_file(
        self,
        file_path: str | Path,
        upload_id: int,
    ) -> ETLResult:
        try:
            records = FileReader.read(file_path)

            original_total = len(records)

            records, duplicate_rows = DataCleaner.remove_duplicates(records)

        except Exception as exc:
            raise ETLReaderError("Failed to read uploaded file.") from exc

        try:
            DataValidator.validate(records)

        except Exception as exc:
            raise ETLValidationError(str(exc)) from exc

        try:
            transformed = DataTransformer.transform(records)

        except Exception as exc:
            raise ETLTransformationError(str(exc)) from exc

        sales = [
            SalesData(
                upload_id=upload_id,
                **record,
            )
            for record in transformed
        ]

        try:
            inserted = DataLoader.bulk_insert(
                self.db,
                sales,
            )

            self.db.commit()

            return ETLResult(
                total_rows=original_total,
                valid_rows=inserted,
                invalid_rows=original_total - inserted - duplicate_rows,
                duplicate_rows=duplicate_rows,
            )

        except SQLAlchemyError as exc:
            self.db.rollback()

            raise ETLLoadError("Failed to save sales data.") from exc

        except Exception:
            self.db.rollback()
            raise
