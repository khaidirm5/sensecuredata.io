"""add users role check constraint

Revision ID: 2c2a4f72398d
Revises: 45734c91b4ef
Create Date: 2026-08-03 21:47:10.047337

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2c2a4f72398d"
down_revision: Union[str, Sequence[str], None] = "45734c91b4ef"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_check_constraint(
        "chk_users_role",
        "users",
        "role IN ('admin', 'analyst', 'user')",
    )


def downgrade() -> None:
    op.drop_constraint(
        "chk_users_role",
        "users",
        type_="check",
    )
