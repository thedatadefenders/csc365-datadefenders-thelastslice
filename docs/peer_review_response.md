# Peer Review Response

# Feature Implementations
* Add pizza recommendation feature, find pizzas by:
	* low-calorie
	* high-protein
	* low-fat

# Code Fixes
* Adjust route paths in pizza.py so that it's just GET /pizza/ and not GET /pizza/pizzas 
* Remove unnecessary/dated code from admin.py that references potions, gold, barrels, etc. 
* Fully convert all calendar references (i.e. /calendar/{date}/pizzas) to use the more descriptive term history instead 
* Fix get_pizzas() N+1 query problem Add pagination to list endpoints 
* Remove auth.py API key printing 
* Adjust imports (some references were missing) while removing unnecessary ones 
* Adjust PUT so that last_updated column is updated 
* Replace POST "/users/get" and POST "/ingredients/get" with GET "users/{user_id" and GET "/ingredients/{ingredient_id}"
# Table Fixes
* Add unique constraints for Users.email and Ingreidents.name to prevent duplicates 
* Add HistoryPizzaRecord quantity to make >= 0 
* Convert Ingredient nutritional values from integers to support fraction values (i.e. 0.5g fat)
* Add foreign keys where necessary, cascade delete