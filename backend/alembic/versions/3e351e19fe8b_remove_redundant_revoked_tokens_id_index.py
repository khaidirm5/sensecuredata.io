from alembic import op

# revision identifiers, used by Alembic.
revision = "3e351e19fe8b"
down_revision = "fdd70bbc440c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_index(
        "ix_revoked_tokens_id",
        table_name="revoked_tokens",
    )


def downgrade() -> None:
    op.create_index(
        "ix_revoked_tokens_id",
        "revoked_tokens",
        ["id"],
        unique=False,
    )
