"""Add Favorites table

Revision ID: e87061601f44
Revises: b243201c5ccc
Create Date: 2026-05-04 04:05:11.334749

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e87061601f44'
down_revision: Union[str, None] = 'b243201c5ccc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "Favorites",
        sa.Column("user_id", sa.Integer, sa.ForeignKey('Users.user_id'), nullable=False),
        sa.Column("pizza_id", sa.Integer, sa.ForeignKey('Pizzas.pizza_id'), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint('user_id', 'pizza_id')
    )



def downgrade() -> None:
    op.drop_table("Favorites")
