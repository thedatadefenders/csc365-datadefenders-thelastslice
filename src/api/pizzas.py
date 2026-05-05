from dataclasses import dataclass
from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, Field, field_validator
from typing import List
from fastapi import HTTPException

import sqlalchemy
from src.api import auth
from src import database as db

router = APIRouter(
    prefix="/pizzas",
    tags=["pizzas"],
    dependencies=[Depends(auth.get_api_key)],
    
)

class IngredientInput(BaseModel):
    ingredientId: int
    amount: int= Field(gt=0)

class PizzaCreate(BaseModel):
    name: str
    ingredients: List[IngredientInput]


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_pizza(pizza: PizzaCreate, user_id = 0):
    with db.engine.begin() as conn:
        result = conn.execute(
            sqlalchemy.text("""
                INSERT INTO "Pizzas" (user_id, name)
                VALUES (:user_id, :name)
                RETURNING pizza_id
            """),
            {"user_id": user_id, "name": pizza.name}
        )

        pizza_id = result.scalar()

        for item in pizza.ingredients:
            conn.execute(
                sqlalchemy.text("""
                    INSERT INTO "PizzaIngredient" (pizza_id, ingredient_id, amount, unit)
                    VALUES (:pizza_id, :ingredient_id, :amount, :unit)
                    """),
                {
                    "pizza_id": pizza_id,
                    "ingredient_id": item.ingredientId,
                    "amount": item.amount,
                    "unit": "grams"
                }
            )

    return {"pizzaId": pizza_id}

@router.get("/pizza/{pizza_id}")
def get_pizza(pizza_id: int):
    with db.engine.connect() as conn:
        pizza = conn.execute(
            sqlalchemy.text("""
                SELECT pizza_id, name
                FROM "Pizzas"
                WHERE pizza_id = :pizza_id
            """),
            {"pizza_id": pizza_id}
        ).fetchone()

        if not pizza:
            raise HTTPException(status_code=404, detail="Pizza not found")

        ingredients = conn.execute(
            sqlalchemy.text("""
                SELECT ingredient_id, amount
                FROM "PizzaIngredient"
                WHERE pizza_id = :pizza_id
            """),
            {"pizza_id": pizza_id}
        ).fetchall()

    return {
        "pizzaId": pizza.pizza_id,
        "name": pizza.name,
        "ingredients": [
            {
                "ingredientId": i.ingredient_id,
                "amount": i.amount
            }
            for i in ingredients
        ]
    }

@router.delete("/{pizza_id}", status_code=status.HTTP_200_OK)
def delete_pizza(pizza_id: int):
    with db.engine.begin() as conn:
        conn.execute(
            sqlalchemy.text("""
                DELETE FROM "PizzaIngredient"
                WHERE pizza_id = :pizza_id
            """),
            {"pizza_id": pizza_id}
        )

        result = conn.execute(
            sqlalchemy.text("""
                DELETE FROM "Pizzas"
                WHERE pizza_id = :pizza_id
                RETURNING pizza_id
            """),
            {"pizza_id": pizza_id}
        )

        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Pizza not found")

    return {"message": "Pizza deleted successfully"}