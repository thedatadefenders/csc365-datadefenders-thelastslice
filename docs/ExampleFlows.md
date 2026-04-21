# Example Flows

## FLOW 1

### Motivation: 
After working out, Henry is trying to hit his protein goals for the day, so he wants a high protein pizza.  However, Henry is unsure about what to have, so he goes to the Last Slice to figure out what’s the most optimal pizza to hit his goal of high protein.


First, Henry requests for all pizzas in the system

* GET /pizzas

Then, the system returns a list of pizzas stored within the database.

	Outputted:
	[
	{
		“pizza _id”: 101
		“name” : High protein chicken pizza
		“Ingridients” : [
			“Thin crust”,
			“Sauce”,
			“chicken “
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
