"""add duplicate threat type

Revision ID: 54e136de28fa
Revises: f8cf7e126a1e
Create Date: 2026-08-06 12:16:33.785579
"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "54e136de28fa"
down_revision: Union[str, Sequence[str], None] = "f8cf7e126a1e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        "chk_security_threat",
        "security_scans",
        type_="check",
    )

    op.create_check_constraint(
        "chk_security_threat",
        "security_scans",
        """
        threat_type IN (
            'NONE',
            'DUPLICATE',
            'MALWARE',
            'MACRO',
            'EXECUTABLE',
            'SUSPICIOUS',
            'UNKNOWN'
        )
        """,
    )


def downgrade() -> None:
    op.drop_constraint(
        "chk_security_threat",
        "security_scans",
        type_="check",
    )

    op.create_check_constraint(
        "chk_security_threat",
        "security_scans",
        """
        threat_type IN (
            'NONE',
            'MALWARE',
            'MACRO',
            'EXECUTABLE',
            'SUSPICIOUS',
            'UNKNOWN'
        )
        """,
    )
