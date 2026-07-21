"""add verdict hash

Revision ID: 963dcd789856
Revises: 0cb22bf6e0a0
Create Date: 2026-07-21 16:48:14.557421

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '963dcd789856'
down_revision: Union[str, Sequence[str], None] = '0cb22bf6e0a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "verdicts",
        sa.Column(
            "verdict_hash",
            sa.String(length=64),
            nullable=True
        )
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column(
        "verdicts",
        "verdict_hash"
    )
    op.create_index(op.f('ix_verdicts_id'), 'verdicts', ['id'], unique=False)
    # ### end Alembic commands ###
