"""Add Pizzas table

Revision ID: b243201c5ccc
Revises: 8e1f524235ca
Create Date: 2026-05-04 03:54:53.697377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b243201c5ccc'
down_revision: Union[str, None] = '8e1f524235ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "Pizzas",
        sa.Column("pizza_id", sa.Integer, primary_key=True, autoincrement=True, nullable=False),
        sa.Column("user_id", sa.Integer, sa.ForeignKey('Users.user_id'), nullable=False),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("last_updated", sa.TIMESTAMP(timezone=True), server_default=sa.func.now(), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("Pizzas")
