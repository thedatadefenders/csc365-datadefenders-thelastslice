# API Specification

### Pizzas

* Add Recipe

  (POST /pizzas)

  Input: 
  {
    "name": "string",
    "ingredients": [
      {
        "ingredientId": "integer",
        "amount": "number"
      }
    ]
  }
  
  Output: 
  {
    "pizzaId": "integer"
  }


* Retrieve All Recipes

  (GET /pizzas)

  Output:
  [
  {
    "pizzaId": "integer",
    "name": "string",
    "ingredients": [
      {
        "ingredientId": "integer",
        "amount": "number"
      }
    ]
  }
  ]


* Retrieve Pizza Recipe

  (GET /pizzas/{pizzaID})

  Output:
  {
    "pizzaId": "integer",
    "name": "string",
    "ingredients": [
      {
        "ingredientId": "integer",
        "amount": "number"
      }
    ]
  }


* Retrieve Nutrition of Pizza

  (GET /pizzas/{pizzaID}/nutrition)

  Output:
  {
    "calories": "number",
    "protein": "number",
    "fat": "number",
    "carbs": "number"
  }


* Delete Pizza Recipe

  (DELETE /pizzas/{pizzaID})

  Output: 204 No Content 


* Update Pizza Recipe

  (PUT /pizzas/{pizzaID})

  Input:
  {
    "name": "string",
    "ingredients": [
      {
        "ingredientId": "integer",
        "amount": "number"
      }
    ]
  }

  Output: 204 No Content 


* Retrieve Pizza Ingredients(READ FUNCTION)

  (GET /pizzas/{pizzaID}/ingredients)

  Output: 
  {
    "ingredients": [
      {
        "ingredientId": "integer",
        "amount": "number"
      }
    ]
  }



### Calendar

* Add Plan for Pizzas to Calendar (WRITE FUNCTION)

  (POST /calendar/{date}/pizzas)

  Input:
  {
    "pizzaId": "integer",
    "quantity": "integer"
  }
  
  Output:
  {
    "date": "string",
    "pizzaId": "integer",
    "quantity": "integer"
  }


* Get Pizzas Planned for the Date from Calendar(READ FUNCTION)

  (GET /calendar/{date}/pizzas)

  Output:
  {
    "date": "string",
    "pizzas": [
      {
        "pizzaId": "integer",
        "quantity": "integer"
      }
    ]
  }
