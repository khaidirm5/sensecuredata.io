"""rename created_at to revoked_at

Revision ID: fdd70bbc440c
Revises: d483b4262352
Create Date: 2026-08-03 22:03:43.976523

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "fdd70bbc440c"
down_revision: Union[str, Sequence[str], None] = "d483b4262352"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "revoked_tokens",
        "created_at",
        new_column_name="revoked_at",
    )


def downgrade() -> None:
    op.alter_column(
        "revoked_tokens",
        "revoked_at",
        new_column_name="created_at",
    )
