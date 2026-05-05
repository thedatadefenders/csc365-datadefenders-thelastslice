## Example Workflow

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



## Testing Results

1. The curl statement called. You can find this in the /docs site under Pizzas, when calling the post /pizzas/ endpoint 
curl call looks like:

        curl -X 'POST' \
          'https://csc365-datadefenders-thelastslice.onrender.com/pizzas/?user_id=0' \
          -H 'accept: application/json' \
          -H 'access_token: TheBestSlice365' \
          -H 'Content-Type: application/json' \
          -d '{
          "name": "Bugolgi Pizza",
          "ingredients": [
            {
              "ingredientId": 1,
              "amount": 3
            }
          ]
        }' 


The response received by calling post is the id number of the pizza just created with the post call:

    {
      "pizzaId": 1
    }

2. Using the pizza id, we can now call this to get the pizza information. The get /pizzas/ endpoint 
curl call looks like:

        curl -X 'GET' \
          'https://csc365-datadefenders-thelastslice.onrender.com/pizzas/pizza/1' \
          -H 'accept: application/json' \
          -H 'access_token: TheBestSlice365' 

The response received by calling get is the information of the pizza initially created with the post call:

    {
      "pizzaId": 1,
      "name": "Bugolgi Pizza",
      "ingredients": [
        {
          "ingredientId": 1,
          "amount": 3
        }
      ]
    } 

3. Following this, with the pizza id, we can also delete the pizza from the database by using delete. The delete /pizzas/ endpoint 
curl call looks like:

          curl -X 'DELETE' \
            'https://csc365-datadefenders-thelastslice.onrender.com/pizzas/1' \
            -H 'accept: application/json' \
            -H 'access_token: TheBestSlice365' 

The response recieved by calling delete is a succesful termination message:

    {
      "message": "Pizza deleted successfully"
    } 
