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

  Output:
  {
    "message": "Pizza deleted successfully"
  }


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



### History

* Add Plan for Pizzas to History (WRITE FUNCTION)

  (POST /history/{date}/pizzas)

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


* Get Pizzas Planned for the Date from History(READ FUNCTION)

  (GET /history/{date}/pizzas)

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
