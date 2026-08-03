"""remove redundant users id index

Revision ID: 45734c91b4ef
Revises: 3b59e9c6899d
Create Date: 2026-08-03 21:36:14.819321

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "45734c91b4ef"
down_revision: Union[str, Sequence[str], None] = "3b59e9c6899d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.drop_index(
        "ix_users_id",
        table_name="users",
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.create_index(
        "ix_users_id",
        "users",
        ["id"],
        unique=False,
    )
