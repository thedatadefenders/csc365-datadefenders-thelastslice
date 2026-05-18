from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, Field
import sqlalchemy
from src.api import auth
from src import database as db
from sqlalchemy.exc import NoResultFound

router = APIRouter(
    prefix="/ingredients",
    tags=["ingredients"],
    dependencies=[Depends(auth.get_api_key)],
)

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_ingredient(name = "", calories_per_unit = 0, protein_per_unit = 0, carbs_per_unit = 0, fats_per_unit = 0):
    if name == "":
        return "Empty name provided, try again"
        
    with db.engine.begin() as conn:
        result = conn.execute(
            sqlalchemy.text("""
                INSERT INTO "Ingredients" (name, calories_per_unit, protein_per_unit, carbs_per_unit, fats_per_unit)
                VALUES (:name, :calories_per_unit, :protein_per_unit, :carbs_per_unit, :fats_per_unit)
                RETURNING ingredient_id
            """),
            {"name": name, "calories_per_unit": calories_per_unit, "protein_per_unit": protein_per_unit, "carbs_per_unit": carbs_per_unit, "fats_per_unit": fats_per_unit}
        )

        ingredient_id = result.scalar()

    return {"ingredient_id": ingredient_id}

@router.post("/get", status_code=status.HTTP_201_CREATED)
def get_ingredient(ingredient_id = 0):
    with db.engine.begin() as conn:
        try: 
            row = conn.execute(
                sqlalchemy.text("""
                    SELECT *
                    FROM "Ingredients"
                    WHERE ingredient_id = :ingredient_id
                """),
                {"ingredient_id": ingredient_id}
            ).one()
        
            name = row.name 
            calories_per_unit = row.calories_per_unit
            protein_per_unit = row.protein_per_unit
            carbs_per_unit = row.carbs_per_unit
            fats_per_unit = row.fats_per_unit
        
        except NoResultFound: 
            return "No ingredient found for that id"

    return {"ingredient_id": ingredient_id, "name": name, "calories_per_unit": calories_per_unit, "protein_per_unit": protein_per_unit, "carbs_per_unit": carbs_per_unit, "fats_per_unit": fats_per_unit}