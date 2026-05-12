## Example Workflow

## FLOW 3
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

## Testing Results

1. The curl statement called. You can find this in the /docs site under Calendar, when calling the POST /calendar/{date}/pizzas endpoint.

curl call looks like:
  curl -X 'POST' \
  'http://127.0.0.1:3000/history/2026-04-21/pizzas?pizza_id=101&quantity=2&user_id=0' \
  -H 'accept: application/json' \
  -H 'access_token: TheBestSlice365' \
  -d ''
  -d '{
    "pizzaId": 101,
    "quantity": 2
  }'

  The response received by calling post is the planned pizza information stored for the selected day:

  {
  "date": "2026-04-21",
  "pizzaId": 101,
  "quantity": 2
  }

2. Next, Owen wants to confirm the pizzas planned for the selected date. The GET /calendar/{date}/pizzas endpoint

curl call looks like:
  curl -X 'GET' \
  'http://127.0.0.1:3000/history/26-04-21/pizzas?user_id=0' \
  -H 'accept: application/json' \
  -H 'access_token: TheBestSlice365'

  The response received by calling get is the list of pizzas scheduled for that day:

  {
  "date": "2026-04-21",
  "pizzas": [
    {
      "pizzaId": 101,
      "quantity": 2
    }
  ]
  }
3. Following this, Owen decides he wants to cook the pizza immediately, so he retrieves the ingredient information for the pizza. The GET /pizzas/{pizzaId}/ingredients endpoint
curl call looks like:

curl -X 'GET' \
  'http://127.0.0.1:3000/pizzas/101/nutrition' \
  -H 'accept: application/json' \
  -H 'access_token: TheBestSlice365'
  {
	"ingredients": [
      { "ingredientId": 1, "amount": 100 },
      { "ingredientId": 2, "amount": 50 },
      { "ingredientId": 3, "amount": 240 },
      { "ingredientId": 4, "amount": 80 }
    ]
  }



