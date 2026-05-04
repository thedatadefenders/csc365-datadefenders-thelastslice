"""Add Ingredients table

Revision ID: f0bbc563e1ee
Revises: 1f1b2b452fa2
Create Date: 2026-05-04 04:13:31.479533

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0bbc563e1ee'
down_revision: Union[str, None] = '1f1b2b452fa2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "Ingredients",
        sa.Column("ingredient_id", sa.Integer, primary_key=True, autoincrement=True, nullable=False),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("calories_per_unit", sa.Integer, nullable=False),
        sa.Column("protein_per_unit", sa.Integer, nullable=False),
        sa.Column("carbs_per_unit", sa.Integer, nullable=False),
        sa.Column("fats_per_unit", sa.Integer, nullable=False),
        sa.CheckConstraint("calories_per_unit >= 0", name="check_calories_positive"),
        sa.CheckConstraint("protein_per_unit >= 0", name="check_protein_positive"),
        sa.CheckConstraint("carbs_per_unit >= 0", name="check_carbs_positive"),
        sa.CheckConstraint("fats_per_unit >= 0", name="check_fats_positive")
    )




def downgrade() -> None:
    op.drop_table("Ingredients")