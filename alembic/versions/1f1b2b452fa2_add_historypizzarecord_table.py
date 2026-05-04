"""Add HistoryPizzaRecord table

Revision ID: 1f1b2b452fa2
Revises: e87061601f44
Create Date: 2026-05-04 04:07:46.282460

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f1b2b452fa2'
down_revision: Union[str, None] = 'e87061601f44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "HistoryPizzaRecord",
        sa.Column("user_id", sa.Integer, sa.ForeignKey('Users.user_id'), nullable=False),
        sa.Column("pizza_id", sa.Integer, sa.ForeignKey('Pizzas.pizza_id'), nullable=False),
        sa.Column("date", sa.Date, server_default=sa.text("CURRENT_DATE"), nullable=False),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint('user_id', 'pizza_id', 'date')
    )

def downgrade() -> None:
    op.drop_table("HistoryPizzaRecord")
