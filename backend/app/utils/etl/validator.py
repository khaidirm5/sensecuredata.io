from datetime import date
from decimal import Decimal


class DataValidator:
    """Validate uploaded sales data."""

    REQUIRED_COLUMNS = {
        "invoice_number",
        "order_date",
        "product_name",
        "category",
        "quantity",
        "unit_price",
        "region",
    }

    @classmethod
    def validate_not_empty(
        cls,
        records: list[dict],
    ) -> None:
        if not records:
            raise ValueError("Uploaded file contains no data.")

    @classmethod
    def validate_columns(
        cls,
        records: list[dict],
    ) -> None:
        columns = set(records[0].keys())

        missing = cls.REQUIRED_COLUMNS - columns

        if missing:
            raise ValueError("Missing required columns: " + ", ".join(sorted(missing)))

    @classmethod
    def validate_data_types(
        cls,
        records: list[dict],
    ) -> None:
        for index, record in enumerate(records, start=1):
            if not isinstance(record["invoice_number"], str):
                raise ValueError(f"Row {index}: invoice_number must be string.")

            if not isinstance(record["product_name"], str):
                raise ValueError(f"Row {index}: product_name must be string.")

            if not isinstance(record["category"], str):
                raise ValueError(f"Row {index}: category must be string.")

            if not isinstance(record["region"], (str, type(None))):
                raise ValueError(f"Row {index}: region must be string.")

            if not isinstance(record["quantity"], int):
                raise ValueError(f"Row {index}: quantity must be integer.")

            if not isinstance(
                record["unit_price"],
                (int, float, Decimal),
            ):
                raise ValueError(f"Row {index}: unit_price must be numeric.")

            if not isinstance(
                record["order_date"],
                (str, date),
            ):
                raise ValueError(f"Row {index}: order_date must be date or string.")

    @classmethod
    def validate_business_rules(
        cls,
        records: list[dict],
    ) -> None:
        for index, record in enumerate(records, start=1):
            if not record["invoice_number"]:
                raise ValueError(f"Row {index}: invoice_number cannot be empty.")

            if not record["product_name"]:
                raise ValueError(f"Row {index}: product_name cannot be empty.")

            if not record["category"]:
                raise ValueError(f"Row {index}: category cannot be empty.")

            if record["quantity"] < 0:
                raise ValueError(
                    f"Row {index}: quantity must be greater than or equal to 0."
                )

            if Decimal(record["unit_price"]) < Decimal("0"):
                raise ValueError(
                    f"Row {index}: unit_price must be greater than or equal to 0."
                )

    @classmethod
    def validate(
        cls,
        records: list[dict],
    ) -> None:
        cls.validate_not_empty(records)
        cls.validate_columns(records)
        cls.validate_data_types(records)
        cls.validate_business_rules(records)
