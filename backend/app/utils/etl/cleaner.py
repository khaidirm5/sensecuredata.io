class DataCleaner:
    """Clean uploaded sales data."""

    @classmethod
    def remove_duplicates(
        cls,
        records: list[dict],
    ) -> tuple[list[dict], int]:
        unique_records: list[dict] = []
        seen: set[tuple] = set()

        duplicates = 0

        for record in records:
            key = (
                str(record["invoice_number"]).strip(),
                str(record["product_name"]).strip(),
                str(record["order_date"]).strip(),
            )

            if key in seen:
                duplicates += 1
                continue

            seen.add(key)
            unique_records.append(record)

        return unique_records, duplicates
