## Example Workflow

## FLOW 1

First, Henry requests for all pizzas in the system

* GET /pizzas

Then, the system returns a list of pizzas stored within the database.

	Outputted:
	{
		“pizza _id”: 101
		“name” : High protein chicken pizza
		“Ingridients” : [
			“Thin crust”,
			“Sauce”,
			“chicken”,
			“Cheese”]
	}
    


Next, Henry scrolls through the list of available pizzas and is trying to find something he likes to eat as well because while he’s still trying to hit his protein goals, he wants to have something yummy. Therefore, he picks the High Protein Chicken Pizza and inquires for its nutrition information

* GET/pizzas/101/nutrition

Prompted, the system returns the nutritional info of the pizza.

	Outputted:
	{
		"calories": 600,
		"protein": 30,
		"fat": 20,
		"carbs": 50
	}

Henry just hit push day, so he’s feeling like he wants some double chicken on his pizza.  Therefore, he decides to update the pizza recipe.

* PUT/pizzas/101/

	  Inputted: 
	  {
	    "name": "Double Protein Chicken Pizza",
	    "ingredients": [
	      { "ingredientId": 1, "amount": 100 },
	      { "ingredientId": 2, "amount": 50 },
	      { "ingredientId": 3, "amount": 240 },
	      { "ingredientId": 4, "amount": 80 }
	    ]
	  }
  
After, Henry wants to see the updated nutritional info of his pizza, so he inquires once again.

* GET/pizzas/101/nutrition

Prompted, the system returns the nutritional info of the pizza.

	  Outputted:
	  {
	    "calories": 750,
	    "protein": 60,
	    "fat": 22,
	    "carbs": 50
	  }

Henry is satisfied with the nutrition, so he decides to cook the recipe and reward himself with a nice and fresh pizza.

## Testing Results

1. The curl statement called. You can find this in the /docs site under Pizzas, when calling the GET /pizzas endpoint.
curl call looks like:

curl -X 'GET' \
  'http://127.0.0.1:3000/pizzas/pizzas' \
  -H 'accept: application/json' \
  -H 'access_token: TheBestSlice365'


The response received by calling get is the list of pizzas currently stored in the database:

  [
  {
    "pizzaId": 101,
    "name": "High Protein Chicken Pizza",
    "ingredients": [
      "Thin crust",
      "Sauce",
      "Chicken",
      "Cheese"
    ]
  }
]

2. Next, using the pizza id, we can now call the nutrition endpoint to retrieve the nutrition information for the selected pizza. The GET /pizzas/{pizzaId}/nutrition endpoint
curl call looks like:

curl -X 'GET' \
  'http://127.0.0.1:3000/pizzas/101/nutrition' \
  -H 'accept: application/json' \
  -H 'access_token: TheBestSlice365'

The response received by calling get is the nutritional information associated with the pizza:

{
	"calories": 600,
	"protein": 30,
	"fat": 20,
	"carbs": 50
}

3. Following this, Henry decides to update the pizza recipe by adding additional chicken to increase the protein amount. The PUT /pizzas/{pizzaId} endpoint
curl call looks like:

curl -X 'PUT' \
  'http://127.0.0.1:3000/pizzas/pizza/101' \
  -H 'accept: application/json' \
  -H 'access_token: TheBestSlice365' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Double Protein Chicken Pizza",
    "ingredients": [
      { "ingredientId": 1, "amount": 100 },
      { "ingredientId": 2, "amount": 50 },
      { "ingredientId": 3, "amount": 240 },
      { "ingredientId": 4, "amount": 80 }
    ]
  }'

  The response received by calling put is a successful update message:
  {
  "message": "Pizza updated successfully"
  }

4. After updating the pizza, Henry once again calls the nutrition endpoint to verify the updated nutrition values. The GET /pizzas/{pizzaId}/nutrition endpoint
  curl call looks like:

  curl -X 'GET' \
  'http://127.0.0.1:3000/pizzas/101/nutrition' \
  -H 'accept: application/json' \
  -H 'access_token: TheBestSlice365'

  The response received by calling get is the updated nutritional information of the modified pizza:
  
  {
  "calories": 750,
  "protein": 60,
  "fat": 22,
  "carbs": 50
}
