"""remove unit from pizza ingredient and unit to ingredients

Revision ID: bd5c89fafc7f
Revises: 2bf0644602f6
Create Date: 2026-06-01 20:45:56.855913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd5c89fafc7f'
down_revision: Union[str, None] = '2bf0644602f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("PizzaIngredient", "unit")
    op.add_column("Ingredients", sa.Column("unit", sa.String(), server_default="1 cup", nullable = False))


def downgrade() -> None:
    op.drop_column("Ingredients", "unit")
    op.add_column("PizzaIngredient", sa.Column("unit", sa.String(), server_default="1 cup", nullable = False))
