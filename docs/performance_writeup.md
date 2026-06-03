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

| Endpoint                           |                         Time (ms) |
| ---------------------------------- | --------------------------------: |
| POST /pizzas/                      |                      **3.301 ms** |
| GET /pizzas/                       |                      **1.730 ms** |
| PUT /pizzas/1                      |                      **0.958 ms** |
| GET /pizzas/1                      |                      **1.018 ms** |
| DELETE /pizzas/1                   |                      **0.763 ms** |
| GET /pizzas/recommend              |        **659.582 ms** *(slowest)* |
| GET /pizzas/1/nutrition            |                      **0.355 ms** |
| POST /pizzas/search-by-ingredients |                    **205.451 ms** |
| POST /history/date/pizzas          |                      **1.099 ms** |
| GET /history/date                  |                      **0.421 ms** |
| POST /ingredients/create           |                      **0.368 ms** |
| GET /ingredients/6                 |                      **0.223 ms** |



# Performance Tuning


Running The Recommend Query with Explain Analyze:

        EXPLAIN ANALYZE
        SELECT p.pizza_id, p.name,
            COUNT(pi.ingredient_id) AS ingredient_count,
            SUM(i.calories_per_unit * pi.amount) AS calories,
            SUM(i.protein_per_unit * pi.amount) AS protein,
            SUM(i.fats_per_unit * pi.amount) AS fat,
            SUM(i.carbs_per_unit * pi.amount) AS carbs
        FROM "Pizzas" p
        JOIN "PizzaIngredient" pi 
            ON p.pizza_id = pi.pizza_id
        JOIN "Ingredients" i 
            ON i.ingredient_id = pi.ingredient_id
        GROUP BY p.pizza_id, p.name
        HAVING COUNT(pi.ingredient_id) <= 5;

Resulting Statement from the Recommend Query: 


    GroupAggregate  (cost=1.23..100367.08 rows=66359 width=162) (actual time=14.197..651.415 rows=199076.00 loops=1)
      Group Key: p.pizza_id
      Filter: (count(pi.ingredient_id) <= 5)
      Buffers: shared hit=10543
      ->  Merge Join  (cost=1.23..68019.07 rows=796251 width=54) (actual time=14.169..349.591 rows=796251.00 loops=1)
            Merge Cond: (pi.pizza_id = p.pizza_id)
            Buffers: shared hit=10543
            ->  Nested Loop  (cost=0.58..50476.93 rows=796251 width=32) (actual time=14.135..253.320 rows=796251.00 loops=1)
                  Buffers: shared hit=7996
    "              ->  Index Scan using ""PizzaIngredient_pkey"" on ""PizzaIngredient"" pi  (cost=0.42..30649.19 rows=796251 width=12) (actual time=14.100..96.119 rows=796251.00 loops=1)"
                        Index Searches: 1
                        Buffers: shared hit=7756
                  ->  Memoize  (cost=0.15..0.17 rows=1 width=24) (actual time=0.000..0.000 rows=1.00 loops=796251)
                        Cache Key: pi.ingredient_id
                        Cache Mode: logical
                        Hits: 796131  Misses: 120  Evictions: 0  Overflows: 0  Memory Usage: 15kB
                        Buffers: shared hit=240
    "                    ->  Index Scan using ""Ingredients_pkey"" on ""Ingredients"" i  (cost=0.14..0.16 rows=1 width=24) (actual time=0.001..0.001 rows=1.00 loops=120)"
                              Index Cond: (ingredient_id = pi.ingredient_id)
                              Index Searches: 120
                              Buffers: shared hit=240
    "        ->  Index Scan using ""Pizzas_pkey"" on ""Pizzas"" p  (cost=0.42..7091.90 rows=199077 width=26) (actual time=0.013..17.788 rows=199077.00 loops=1)"
                  Index Searches: 1
                  Buffers: shared hit=2547
    Planning:
      Buffers: shared hit=33 dirtied=1
    Planning Time: 1.394 ms
    JIT:
      Functions: 21
      Options: Inlining false, Optimization false, Expressions true, Deforming true
      Timing: Generation 2.115 ms (Deform 0.680 ms), Inlining 0.000 ms, Optimization 1.382 ms, Emission 12.699 ms, Total 16.195 ms
    Execution Time: 658.188 ms

3 Indexs are already used within our query, speeding up the query sufficiently for our service. This makes the next logical scenario to seek improvement in execution at the code itself.  Inherently speaking, since this functions queries basically almost the entire database, fixes to this could be to consoldiate information beforhand like generating the totals of nutritional info beforehand.









