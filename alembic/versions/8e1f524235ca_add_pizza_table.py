"""Add Users table

Revision ID: 8e1f524235ca
Revises: 
Create Date: 2026-05-04 02:50:40.393110

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e1f524235ca'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "Users",
        sa.Column("user_id", sa.Integer, primary_key=True, autoincrement=True, nullable=False),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("email", sa.String, nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.func.now())
    )

def downgrade() -> None:
    op.drop_table("Users")
