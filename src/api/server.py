from fastapi import FastAPI
from src.api import admin, favorites, history, ingredients, pizzas, users
from starlette.middleware.cors import CORSMiddleware

description = """
The Last Slice is the premier tracking site for all your pizza needs. 
Whether you're a pizza connoisseur or just looking for a quick slice, we've got you covered. 
"""
tags_metadata = [
    {"name": "pizzas", "description": "Make and get pizza recipes"},
    {"name": "users", "description": "Make and see users"},
    {"name": "history", "description": "View previously made pizzas"},
    {"name": "favorites", "description": "Save and retrieve your favorite recipes!"},
    {"name": "ingredients", "description": "Make and see ingredients"},
    {"name": "admin", "description": "Where you reset the database."},
]

app = FastAPI(
    title="The Last Slice API",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Aaron Lee",
        "email": "alee670@calpoly.edu",
    },
    openapi_tags=tags_metadata,
)

origins = [
    "https://thelastslice.vercel.app",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pizzas.router)
app.include_router(history.router)
app.include_router(favorites.router)
app.include_router(ingredients.router)
app.include_router(users.router)
app.include_router(admin.router)


@app.get("/")
async def root():
    return {"message": "Time To Get The Last Slice!"}
