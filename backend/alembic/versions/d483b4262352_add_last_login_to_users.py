"""add last login to users

Revision ID: d483b4262352
Revises: 2c2a4f72398d
Create Date: 2026-08-03 21:50:22.003088

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d483b4262352"
down_revision: Union[str, Sequence[str], None] = "2c2a4f72398d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "last_login",
            sa.DateTime(timezone=True),
            nullable=True,
        ),
    )


def downgrade() -> None:
    op.drop_column(
        "users",
        "last_login",
    )
