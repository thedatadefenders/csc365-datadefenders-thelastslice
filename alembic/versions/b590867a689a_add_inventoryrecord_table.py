"""Add InventoryRecord table

Revision ID: b590867a689a
Revises: f0bbc563e1ee
Create Date: 2026-05-04 04:16:43.541718

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b590867a689a'
down_revision: Union[str, None] = 'f0bbc563e1ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "InventoryRecord",
        sa.Column("user_id", sa.Integer, sa.ForeignKey('Users.user_id'), nullable=False),
        sa.Column("ingredient_id", sa.Integer, sa.ForeignKey('Ingredients.ingredient_id'), nullable=False),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.Column("last_updated", sa.TIMESTAMP(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint('user_id', 'ingredient_id')
    )


def downgrade() -> None:
    op.drop_table("InventoryRecord")
