import random
import sys
from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from app.db.database import engine
from app.models.sales_data import SalesData
from app.models.upload_history import UploadHistory
from scripts.data import (
    MAX_QUANTITY,
    MIN_QUANTITY,
    PRODUCTS,
    REGIONS,
)

TOTAL_RECORDS = 5000

START_DATE = date(2024, 1, 1)
END_DATE = date(2026, 8, 1)


def random_date() -> date:
    days = (END_DATE - START_DATE).days
    return START_DATE + timedelta(days=random.randint(0, days))


def seed_sales(db: Session) -> None:
    """Seed sales data."""

    print(f"Seeding {TOTAL_RECORDS} sales records...")

    upload = db.scalar(select(UploadHistory).order_by(UploadHistory.id.desc()))

    if upload is None:
        print("No upload history found.")
        return

    sales: list[SalesData] = []

    for i in range(1, TOTAL_RECORDS + 1):
        product = random.choice(PRODUCTS)

        quantity = random.randint(
            MIN_QUANTITY,
            MAX_QUANTITY,
        )

        unit_price: Decimal = product["price"]

        total_price = unit_price * quantity

        sale = SalesData(
            upload_id=upload.id,
            invoice_number=f"INV-{i:06d}",
            order_date=random_date(),
            product_name=product["name"],
            category=product["category"],
            quantity=quantity,
            unit_price=unit_price,
            total_price=total_price,
            region=random.choice(REGIONS),
        )

        sales.append(sale)

    db.add_all(sales)
    db.commit()

    print(f"Inserted {len(sales)} sales records successfully.")


def main() -> None:
    with Session(engine) as db:
        seed_sales(db)


if __name__ == "__main__":
    main()
