from datetime import date, datetime
from decimal import Decimal


class DataTransformer:
    """Transform uploaded sales data."""

    @classmethod
    def transform(
        cls,
        records: list[dict],
    ) -> list[dict]:
        transformed: list[dict] = []

        for record in records:
            invoice_number = record["invoice_number"].strip()

            product_name = record["product_name"].strip()

            category = cls.normalize_category(
                record["category"],
            )

            region = cls.normalize_region(
                record.get("region"),
            )

            quantity = int(record["quantity"])

            unit_price = Decimal(str(record["unit_price"]))

            transformed.append(
                {
                    "invoice_number": invoice_number,
                    "order_date": cls.parse_date(
                        record["order_date"],
                    ),
                    "product_name": product_name,
                    "category": category,
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "total_price": unit_price * quantity,
                    "region": region,
                }
            )

        return transformed

    @staticmethod
    def parse_date(
        value: str | date | datetime,
    ) -> date:
        if isinstance(value, datetime):
            return value.date()

        if isinstance(value, date):
            return value

        return datetime.strptime(
            value,
            "%Y-%m-%d",
        ).date()

    @staticmethod
    def normalize_category(
        value: str,
    ) -> str:
        return " ".join(
            value.strip().split(),
        ).title()

    @staticmethod
    def normalize_region(
        value: str | None,
    ) -> str:
        if value is None:
            return "Unknown"

        value = value.strip()

        if not value:
            return "Unknown"

        return " ".join(
            value.split(),
        ).title()
