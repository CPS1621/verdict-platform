"""add verdict supersession fields

Revision ID: 072d157c3cab
Revises: 963dcd789856
Create Date: 2026-07-23 15:07:05.532991
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "072d157c3cab"
down_revision: Union[str, Sequence[str], None] = "963dcd789856"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column(
        "verdict_events",
        sa.Column(
            "is_superseded",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
        ),
    )

    op.add_column(
        "verdict_events",
        sa.Column(
            "superseded_by",
            sa.Integer(),
            nullable=True,
        ),
    )


def downgrade() -> None:

    op.drop_column("verdict_events", "superseded_by")
    op.drop_column("verdict_events", "is_superseded")