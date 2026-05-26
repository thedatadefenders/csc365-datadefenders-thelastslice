from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, Field
from typing import List, Annotated
from datetime import date
from fastapi import HTTPException


import sqlalchemy
from src.api import auth
from src import database as db

from src.api import auth

router = APIRouter(
    prefix="/history",
    tags=["history"],
    dependencies=[Depends(auth.get_api_key)],
)

@router.post("/{pizza_date}/pizzas", status_code=status.HTTP_201_CREATED)
def add_pizza_to_history(
    pizza_date: date,
    pizza_id: int,
    quantity: int,
    user_id: int = 0
):

    with db.engine.begin() as conn:

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

        conn.execute(
            sqlalchemy.text("""
                INSERT INTO "HistoryPizzaRecord"
                (user_id, pizza_id, date, quantity)
                VALUES (:user_id, :pizza_id, :date, :quantity)
            """),
            {
                "user_id": user_id,
                "pizza_id": pizza_id,
                "date": pizza_date,
                "quantity": quantity
            }
        )

    return {
        "date": pizza_date,
        "pizzaId": pizza_id,
        "quantity": quantity
    }

@router.get("/{pizza_date}/pizzas")
def get_history_pizzas(
    pizza_date: date,
    user_id: int = 0
):
    with db.engine.connect() as conn:
        rows = conn.execute(
            sqlalchemy.text("""
                SELECT pizza_id, quantity
                FROM "HistoryPizzaRecord"
                WHERE user_id = :user_id AND date = :date
            """),
            {
                "user_id": user_id,
                "date": pizza_date
            }
        ).fetchall()

    return {
        "date": pizza_date,
        "pizzas": [
            {
                "pizzaId": row.pizza_id,
                "quantity": row.quantity
            }
            for row in rows
        ]
    }