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



## FLOW 2

### Motivation:
Aaron wants to create his own custom pizza because none of the current options match his taste and he has an extensive allergy list. After creating it, he wants to verify the recipe and ingredients to make sure everything is correct. The Last Slice offers all of this functionality, so he wants to check it out and see if he can make a pizza that he truly wants.


First, Aaron decides to create his own pizza recipe.

* POST /pizzas

		Inputted:
		{
		  "name": "Bugolgi Pizza",
		  "ingredients": [
			{ "ingredientId": 5, "amount": 100 },
			{ "ingredientId": 2, "amount": 50 },
			{ "ingredientId": 6, "amount": 120 }
		  ]
		}

Then, the system returns an id associated with the pizza.

	Outputted:
	{
	  "pizzaId": 202
	}

Next, Aaron wants to view the full details of the pizza he just created.

* GET /pizzas/202

Then, the system returns the pizza associated with the id stored within the database.

	Outputted:
	{
	  "pizzaId": 202,
	  "name": "Bugolgi Pizza",
	  "ingredients": [
	    { "ingredientId": 5, "amount": 100 },
	    { "ingredientId": 2, "amount": 50 },
	    { "ingredientId": 6, "amount": 120 }
	  ]
	}

After seeing the recipe and the ingredients once again, Aaron realizes that he’s allergic to beef, so the Bugolgi Pizza isn’t a viable option for him. Therefore, he decides to delete the pizza recipe from the system. 

* DELETE /pizzas/202

The recipe has been deleted, and sadly Aaron is still hungry for pizza.  

## FLOW 3

### Motivation:
Owen wants to plan his meals ahead of time, and the Last Slice offers the option for him to plan his meals ahead of time. Therefore, he decides to give the Last Slice a shot.

First, Owen schedules a pizza for a specific day.

* POST /calendar/2026-04-21/pizzas

		Inputted:
		{
		  "pizzaId": 101,
		  "quantity": 2
		}

Then, the system stores the planned pizza.

	Outputted:
	{
	  "date": "2026-04-21",
	  "pizzaId": 101,
	  "quantity": 2
	}

Next, Owen wants to confirm what he has planned for that day.

* GET /calendar/2026-04-21/pizzas

		Outputted:
		{
		  "date": "2026-04-21",
		  "pizzas": [
		    { "pizzaId": 101, "quantity": 2 }
		  ]
		}

Consequently, Owen decides he wants to cook the pizza now, so he needs the ingredients.

* GET/pizzas/101/ingredients

		Outputted:
		{
		  "ingredients": [
		    { "ingredientId": 1, "amount": 100 },
		    { "ingredientId": 2, "amount": 50 },
		    { "ingredientId": 3, "amount": 120 },
		    { "ingredientId": 4, "amount": 80 }
		  ]
		}

Lastly, Owen is happy with the Last Slice, so he delivers a glowing review.
