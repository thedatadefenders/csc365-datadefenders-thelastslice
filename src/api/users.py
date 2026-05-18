from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, Field
import sqlalchemy
from src.api import auth
from src import database as db
from sqlalchemy.exc import NoResultFound

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(auth.get_api_key)],
)

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(name = "", email = ""):
    if name == "" or email == "":
        return "Empty name or empty email provided, try again"
        
    with db.engine.begin() as conn:
        result = conn.execute(
            sqlalchemy.text("""
                INSERT INTO "Users" (name, email)
                VALUES (:name, :email)
                RETURNING user_id
            """),
            {"name": name, "email": email}
        )

        user_id = result.scalar()

    return {"user_id": user_id}

@router.post("/get", status_code=status.HTTP_201_CREATED)
def get_user(user_id = 0):
    with db.engine.begin() as conn:
        try: 
            row = conn.execute(
                sqlalchemy.text("""
                    SELECT *
                    FROM "Users"
                    WHERE user_id = :user_id
                """),
                {"user_id": user_id}
            ).one()
        
            name = row.name 
            email = row.email
            created_at = row.created_at
        
        except NoResultFound: 
            return "No user found for that id"

    return {"user_id": user_id, "name": name, "email": email, "created_at": created_at}