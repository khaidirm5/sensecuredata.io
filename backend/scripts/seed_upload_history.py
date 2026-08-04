import sys
from pathlib import Path

from sqlalchemy.orm import Session

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from app.db.database import engine
from app.models.upload_history import UploadHistory


def seed_upload_history(db: Session) -> None:
    print("Seeding upload history...")

    upload = UploadHistory(
        uploaded_by=1,
        filename="sales_2026_august.csv",
        file_type="csv",
        total_rows=1000,
        valid_rows=995,
        invalid_rows=5,
        status="SUCCESS",
        error_message=None,
    )

    db.add(upload)
    db.commit()
    db.refresh(upload)

    print(f"Upload History created with ID: {upload.id}")


def main() -> None:
    with Session(engine) as db:
        seed_upload_history(db)


if __name__ == "__main__":
    main()
