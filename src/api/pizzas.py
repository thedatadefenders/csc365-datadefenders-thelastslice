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

@router.put("/{pizza_id}")
def put_pizza(pizza_id: int, pizza: PizzaCreate):
    with db.engine.begin() as conn:
        # Does pizza exist?
        exists = conn.execute(
            sqlalchemy.text(
                """
                SELECT pizza_id
                FROM "Pizzas"
                WHERE pizza_id = :pizza_id
                """
            ),
            {"pizza_id": pizza_id}
        ).fetchone()

        if not exists:
            raise HTTPException(status_code=404, detail="Pizza not found")
        
        conn.execute(
            sqlalchemy.text(
                """
                UPDATE "Pizzas"
                SET name = :name
                WHERE pizza_id = :pizza_id
                """
            ), 
            {"pizza_id": pizza_id, "name": pizza.name}
        )

        # Delete all ingredients
        conn.execute(
            sqlalchemy.text(
                """
                DELETE FROM "PizzaIngredient"
                WHERE pizza_id = :pizza_id
                """
            ), 
            {"pizza_id": pizza_id}
        )

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
    return {
        "message": "Updated pizza",
        "pizzaId": pizza_id
        }

@router.get("/{pizza_id}")
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

@router.get("/")
def get_pizzas():
    with db.engine.connect() as conn:
        rows = conn.execute(
            sqlalchemy.text("""
                SELECT p.pizza_id, name, ingredient_id, amount
                FROM "Pizzas" p
                LEFT JOIN "PizzaIngredient" pi ON p.pizza_id = pi.pizza_id
            """),
        )

        if not rows:
            raise HTTPException(status_code=404, detail="No pizzas found")
        
        pizzas = {}

        for row in rows:
            pizza_id = row.pizza_id
            if pizza_id not in pizzas:
                pizzas[pizza_id] = {
                    "pizzaId": row.pizza_id,
                    "name": row.name,
                    "ingredients": []
                }
            
            if row.ingredient_id is not None:
                pizzas[pizza_id]["ingredients"].append({
                    "ingredientId": row.ingredient_id,
                    "amount": row.amount
                })
        
        return list(pizzas.values())
    
@router.get("/{pizza_id}/nutrition")
def get_pizza_nutrition(pizza_id: int):
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

        row = conn.execute(
            sqlalchemy.text("""
                SELECT 
                    SUM(calories_per_unit * amount) as calories, 
                    SUM(protein_per_unit * amount) as protein, 
                    SUM(fats_per_unit * amount) as fat, 
                    SUM(carbs_per_unit * amount) as carbs
                FROM "PizzaIngredient"
                JOIN "Ingredients" ON "PizzaIngredient".ingredient_id = "Ingredients".ingredient_id
                WHERE pizza_id = :pizza_id
            """),
            {"pizza_id": pizza_id}
        ).fetchone()

        return {
            "calories": row.calories,
            "protein": row.protein,
            "fat": row.fat,
            "carbs": row.carbs,
        }
    
@router.get("/{pizza_id}/ingredients")
def get_pizza_ingredients(pizza_id: int):
    with db.engine.connect() as conn:
        pizza = conn.execute(
            sqlalchemy.text("""
                SELECT pizza_id
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
        "ingredients": [
            {
                "ingredientId": row.ingredient_id,
                "amount": row.amount
            }
            for row in ingredients
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
