## Concurrency Control

### Case 1: Lost Update

Two users each call PUT/pizzas/101 at the same time. Both try to update the pizza by adding ingredients. Without concurrency control, both transactions operate on the same items, each one creating their own version, and one will overwrite the other resulting in one update being lost.

To solve this, we will use pessimistic concurrency control to lock the pizzas table. This doesn't entirely solve the issue of lost updates but will help prevent concurrency issues of changes happening at the same time. For lost updates, we think it's not worth it space-wise to keep a history of every update made to a pizza for a very rare occurence of people updating pizzas at the same time, so we instead update the user_id of the pizza to whoever updated the pizza last so if there are any concurrency issues, it's clear who was the last person to update and who's update got overwritten. 

Sequence diagram: User 1 calls put/pizzas/101 to update pizza 101. While that transaction is in progress, user 2 calls put/pizzas/101 to update pizza 101 but gets stopped by the lock placed on pizzas. User 1's transaction is finished and user 2 calls their transaction. Although user 1's transaction is overwritten, no errors occur and user 2 is marked as the last updater of the pizza, making clear the blame for who last updated.

### Case 2: Non-repeatable Read

GET/pizzas/101/nutrition computes the macros of a pizza and displays the output. A non-repeatable read could happen if this transaction reads the pizza’s ingredient data, but before the transaction finishes, another transaction updates the ingredients for that same pizza.

### Case 3: Phantom Read

The meal planner exposes the endpoint GET /calendar/{date}/total_nutrition, which calculates the total macros for all pizzas scheduled on a specific day. A phantom read could occur if the transaction begins by querying all calendar entries for that date and collecting the (pizzaId, quantity) pairs needed for the nutrition calculation. While this transaction is still processing, another transaction could execute POST /calendar/2026-04-21/pizzas and insert a new pizza entry for that same date.
