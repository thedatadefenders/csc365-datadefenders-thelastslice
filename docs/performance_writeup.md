# Fake Data Modeling
Code can be found in admin.py.

Final rows of data: 
120     in Ingredients
100,000 in Users
199,077 in Pizzas
796,254 in PizzaIngredient
199,077 in HistoryPizzaRecord
TOTAL: 1294408

Ingredients has the lowest amount of rows because we'd want to create something more centralized with a wide breadth of ingredients that comes pre-tracked with nutritional information. We brute forced this and generated random nutritional information for each ingredient. We also made it so that doughs took up ids 1-10, sauces took up ids 11-20, and other toppings took up ids 21-120. We believe there would probably be the most variation in toppings while sauces and doughs would typically stay similar throughout pizzas. 

Users being 100k was an arbitrary number we came up with. 

To get to around 200k pizzas, we gave each user a distribution averaging 2 pizzas. Some users could have none, while others could have upwards of 6. This would be expected as some people might download the app or create an account without ever doing anything, while some diehards would store many recipes.

For each pizza, we guaranteed 2 ingredients every time, a selection of a dough and a sauce. We also gave it a random number of toppings from 1-3. This made it so, on average, each pizza had 4 ingredients, averaging at around 800k total pizza ingredient rows. We thought this made the most sense as our definition of a pizza would require some kind of dough and sauce and probably a topping or two to make it not so boring.

Finally keeping things simple, History pizza record just tracked each recipe as being made once. While they can be made and tracked multiple times, we did this for ease. 

The only realistic thing I would change about this faked data would be the history pizza record having multiple instances of a user making a pizza on different days. This would be harder to do since we do not allow users to add to their history the same pizza on the same day, meaning possible collisions could occur with the randomized dates. To make our primary key, we had to do a composite key of users, pizzas, and dates, so to remedy multiple of the same pizza on one day, we added a column for quantity of pizzas. 


# Performance Results



# Performance Tuning
