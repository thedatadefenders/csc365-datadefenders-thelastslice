from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from typing import List, Annotated

from src.api import auth

router = APIRouter(
    prefix="/history",
    tags=["history"],
    dependencies=[Depends(auth.get_api_key)],
)

