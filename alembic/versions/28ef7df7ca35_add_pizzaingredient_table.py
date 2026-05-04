"""Add PizzaIngredient table

Revision ID: 28ef7df7ca35
Revises: b590867a689a
Create Date: 2026-05-04 04:19:40.140686

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28ef7df7ca35'
down_revision: Union[str, None] = 'b590867a689a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "PizzaIngredient",
        sa.Column("pizza_id", sa.Integer, sa.ForeignKey('Pizzas.pizza_id'), nullable=False),
        sa.Column("ingredient_id", sa.Integer, sa.ForeignKey('Ingredients.ingredient_id'), nullable=False),
        sa.Column("amount", sa.Integer, nullable=False),
        sa.Column("unit", sa.String, nullable=False),
        sa.PrimaryKeyConstraint('pizza_id', 'ingredient_id'),
        sa.CheckConstraint("amount >= 0", name="check_amount_positive")
    )


def downgrade() -> None:
    op.drop_table("PizzaIngredient")
