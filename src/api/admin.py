from fastapi import APIRouter, Depends, status
import sqlalchemy
from src.api import auth
from src import database as db
import os
import dotenv
from faker import Faker
import numpy as np

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(auth.get_api_key)],
)

class Ingredient:
    def __init__(self, name, cals, proteins, carbs, fats, unit):
        self.name = name
        self.cals = cals
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats
        self.unit = unit

doughs = [
    "Traditional Dough",
    "Thin Crust",
    "Thick Crust",
    "Neapolitan Dough",
    "Sourdough",
    "Whole Wheat Dough",
    "Gluten-Free Dough",
    "Cauliflower Crust",
    "Stuffed Crust",
    "Detroit Style Dough",
]

sauces = [
    "Classic Tomato Sauce",
    "Spicy Tomato Sauce",
    "Marinara",
    "Garlic Parmesan Sauce",
    "Alfredo Sauce",
    "Pesto Sauce",
    "BBQ Sauce",
    "Buffalo Sauce",
    "Ranch Sauce",
    "Olive Oil Base",
]

toppings = [
    "Pepperoni", "Sausage", "Bacon", "Ham", "Chicken",
    "Ground Beef", "Meatballs", "Prosciutto", "Salami", "Chorizo",
    "Anchovies", "Tuna", "Shrimp", "Pulled Pork", "Turkey",
    "Mozzarella", "Cheddar", "Parmesan", "Provolone", "Feta",
    "Goat Cheese", "Ricotta", "Blue Cheese", "Swiss", "Vegan Cheese",
    "Mushrooms", "Onions", "Red Onions", "Green Peppers", "Red Peppers",
    "Yellow Peppers", "Jalapeños", "Banana Peppers", "Tomatoes", "Cherry Tomatoes",
    "Black Olives", "Green Olives", "Spinach", "Arugula", "Kale",
    "Broccoli", "Artichokes", "Eggplant", "Zucchini", "Corn",
    "Pineapple", "Sun-Dried Tomatoes", "Garlic", "Basil", "Oregano",
    "Parsley", "Cilantro", "Rosemary", "Thyme", "Capers",
    "Pickles", "Avocado", "Roasted Red Peppers", "Caramelized Onions", "Scallions",
    "Truffle Oil", "Hot Honey", "BBQ Chicken", "Buffalo Chicken", "Steak",
    "Pastrami", "Canadian Bacon", "Duck", "Lamb", "Tofu",
    "Tempeh", "Vegan Sausage", "Vegan Pepperoni", "Kimchi", "Sauerkraut",
    "Gorgonzola", "Brie", "Camembert", "Pecorino", "Asiago",
    "Pesto Drizzle", "Balsamic Glaze", "Crushed Red Pepper", "Sesame Seeds", "Everything Seasoning",
    "Fried Egg", "Hard-Boiled Egg", "Potatoes", "Sweet Potatoes", "Mac and Cheese",
    "Fried Onions", "Crushed Chips", "Pepperoncini", "Cucumber", "Watercress", "Pine Nuts", "Cinammon", "Burrata", "Mint", "Apple"
]

@router.post("/reset", status_code=status.HTTP_204_NO_CONTENT)
def reset():
    total_pizzas = 0
    total_pizza_ingredients = 0
    ingredients = []

    rng = np.random.default_rng()

    for name in doughs:
        ingredients.append(Ingredient(name, 
                                      rng.integers(220, 300),
                                      rng.integers(6, 8),
                                      rng.integers(35, 42),
                                      rng.integers(1, 3),
                                      "200 grams"))
        
    for name in sauces:
        ingredients.append(Ingredient(name, 
                                      rng.integers(15, 100),
                                      rng.integers(1, 5),
                                      rng.integers(1, 3),
                                      rng.integers(1, 8),
                                      "1 cup"))

    for name in toppings:
        ingredients.append(Ingredient(name, 
                                      rng.integers(20, 300),
                                      rng.integers(2, 24),
                                      rng.integers(1, 10),
                                      rng.integers(1, 15),
                                      "1 cup"))

    with db.engine.begin() as connection:
        connection.execute(
            sqlalchemy.text(
                """
                TRUNCATE TABLE "Users", "Pizzas", "Ingredients", "HistoryPizzaRecord", "PizzaIngredient"
                RESTART IDENTITY CASCADE
                """
            )
        )
        for i in ingredients:
            connection.execute(
                sqlalchemy.text(
                    """
                    INSERT INTO "Ingredients" (name, calories_per_unit, protein_per_unit, carbs_per_unit, fats_per_unit, unit)
                    VALUES (:name, :cals, :proteins, :carbs, :fats, :unit)
                    """
                    ), {"name": i.name, "cals": i.cals, "proteins": i.proteins, "carbs": i.carbs, "fats": i.fats, "unit": i.unit})

    
    num_users = 100000
    fake = Faker()
    pizzas_sample_distribution = np.random.default_rng().negative_binomial(2, 0.50, num_users)

    
    with db.engine.begin() as connection:
        for i in range(num_users):
            if (i % 100 == 0):
                print(i)
        
            username = fake.name()
            email = fake.unique.email()
            created_at = fake.date_time_between(start_date='-5y', end_date='now', tzinfo=None)

            user_id = connection.execute(
                sqlalchemy.text(
                    """
                    INSERT INTO "Users" (name, email, created_at)
                    VALUES (:username, :email, :created_at)
                    RETURNING user_id
                    """
                ), {"username": username, "email": email, "created_at": created_at}
            ).scalar_one()

            num_pizzas = pizzas_sample_distribution[i]
            for j in range(num_pizzas):
                total_pizzas += 1

                pizza_id = connection.execute(
                    sqlalchemy.text(
                        """
                        INSERT INTO "Pizzas" (user_id, name, created_at, last_updated)
                        VALUES (:user_id, :name, :created_at, :last_updated)
                        RETURNING pizza_id
                        """
                    ), 
                    {
                    "user_id": user_id,
                    "name": f"{fake.color_name().capitalize()} {fake.word().capitalize()} Pizza", 
                    "created_at": fake.date_time_between(start_date='-5y', end_date='-2y', tzinfo=None),
                    "last_updated": fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None),
                    }
                ).scalar_one()

                pizza_ingredients = []
                pizza_history = []
                
                dough_id = rng.integers(1, 11)
                sauce_id = rng.integers(11, 21)
                num_ing = rng.integers(1, 4)
                ing_ids = rng.choice(range(21, 121), size=num_ing, replace=False)
                total_pizza_ingredients += 2 + num_ing

                pizza_ingredients.append({
                    "pizza_id": pizza_id,
                    "ingredient_id": dough_id,
                    "amount": rng.choice([1, 2, 3, 4], p=[0.75, 0.15, 0.099, 0.001])
                })
                pizza_ingredients.append({
                    "pizza_id": pizza_id,
                    "ingredient_id": sauce_id,
                    "amount": rng.choice([1, 2, 3, 4], p=[0.75, 0.15, 0.099, 0.001])
                })
                for n in ing_ids:
                    pizza_ingredients.append({
                        "pizza_id": pizza_id,
                        "ingredient_id": n,
                        "amount": rng.choice([1, 2, 3, 4], p=[0.75, 0.15, 0.099, 0.001])
                })

                date = fake.date_time_between(start_date='-5y', end_date='now', tzinfo=None)
                quantity = rng.choice([1, 2, 3, 4, 5, 6, 7, 8], p=[0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125, 0.0078125])
                pizza_history.append({"user_id": user_id, "pizza_id": pizza_id, "date": date, "quantity": quantity})

                connection.execute(
                    sqlalchemy.text(
                        """
                        INSERT INTO "PizzaIngredient" (pizza_id, ingredient_id, amount)
                        VALUES (:pizza_id, :ingredient_id, :amount)
                        """
                    ), pizza_ingredients
                )

                connection.execute(
                    sqlalchemy.text(
                        """
                        INSERT INTO "HistoryPizzaRecord" (user_id, pizza_id, date, quantity)
                        VALUES (:user_id, :pizza_id, :date, :quantity)
                        """
                    ), pizza_history
                )

    print("total pizzas:", total_pizzas)
    print("total pizza ingredients:", total_pizza_ingredients)