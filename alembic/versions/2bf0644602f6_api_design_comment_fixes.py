"""API Design comment fixes

Revision ID: 2bf0644602f6
Revises: 28ef7df7ca35
Create Date: 2026-05-26 05:53:29.636751

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2bf0644602f6'
down_revision: Union[str, None] = '28ef7df7ca35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_check_constraint("check_pizza_name_nonempty", "Pizzas", "length(trim(name)) > 0")
    op.create_check_constraint("check_history_quantity_nonnegative", "HistoryPizzaRecord", "quantity > 0")
    op.create_foreign_key("fk_pizzaingredient_ingredient", "PizzaIngredient", "Ingredients", ["ingredient_id"], ["ingredient_id"], ondelete="RESTRICT")
    op.create_unique_constraint("uq_users_email", "Users", ["email"])
    op.create_unique_constraint("uq_ingredients_name", "Ingredients", ["name"])
    op.alter_column("Ingredients", "calories_per_unit", type_=sa.Numeric(10, 2), existing_type=sa.Integer, postgresql_using="calories_per_unit::numeric")
    op.alter_column( "Ingredients", "protein_per_unit", type_=sa.Numeric(10, 2), existing_type=sa.Integer, postgresql_using="protein_per_unit::numeric" )
    op.alter_column( "Ingredients", "carbs_per_unit", type_=sa.Numeric(10, 2), existing_type=sa.Integer, postgresql_using="carbs_per_unit::numeric" )
    op.alter_column( "Ingredients", "fats_per_unit", type_=sa.Numeric(10, 2), existing_type=sa.Integer, postgresql_using="fats_per_unit::numeric" )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("check_pizza_name_nonempty", "Pizzas")
    op.drop_constraint( "check_history_quantity_nonnegative", "HistoryPizzaRecord", )
    op.drop_constraint("fk_pizzaingredient_ingredient", "PizzaIngredient")
    op.drop_constraint("uq_users_email", "Users")
    op.drop_constraint("uq_ingredients_name", "Ingredients")
    op.alter_column( "Ingredients", "calories_per_unit", type_=sa.Integer, existing_type=sa.Numeric, postgresql_using="round(calories_per_unit)" )
    op.alter_column( "Ingredients", "protein_per_unit", type_=sa.Integer, existing_type=sa.Numeric, postgresql_using="round(protein_per_unit)" )
    op.alter_column( "Ingredients", "carbs_per_unit", type_=sa.Integer, existing_type=sa.Numeric, postgresql_using="round(carbs_per_unit)" )
    op.alter_column( "Ingredients", "fats_per_unit", type_=sa.Integer, existing_type=sa.Numeric, postgresql_using="round(fats_per_unit)" )
    pass
