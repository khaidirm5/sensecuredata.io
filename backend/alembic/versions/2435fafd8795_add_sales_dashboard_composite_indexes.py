from typing import Sequence, Union

from alembic import op

# revision identifiers
revision: str = "2435fafd8795"
down_revision: Union[str, Sequence[str], None] = "3e351e19fe8b"
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_index(
        "idx_sales_date_category",
        "sales_data",
        ["order_date", "category"],
    )

    op.create_index(
        "idx_sales_date_region",
        "sales_data",
        ["order_date", "region"],
    )


def downgrade() -> None:

    op.drop_index(
        "idx_sales_date_region",
        table_name="sales_data",
    )

    op.drop_index(
        "idx_sales_date_category",
        table_name="sales_data",
    )
