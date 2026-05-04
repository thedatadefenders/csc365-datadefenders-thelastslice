from dataclasses import dataclass
from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, Field, field_validator
from typing import List

import sqlalchemy
from src.api import auth
from src import database as db

router = APIRouter(
    prefix="/pizzas",
    tags=["pizzas"],
    dependencies=[Depends(auth.get_api_key)],
)

