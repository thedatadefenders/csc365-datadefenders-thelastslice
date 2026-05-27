## Concurrency Control

### Case 1: Lost Update

Two users each call PUT/pizzaz/101 at the same time. Both try to update the pizza by adding ingredients. Without concurrency control, both transactions operate on the same items, each one creating their own version, and one will overwrite the other resulting in one update being lost.

### Case 2: Non-repeatable Read

GET/pizzas/101/nutrition computes the macros of a pizza and displays the output. A non-repeatable read could happen if this transaction reads the pizza’s ingredient data, but before the transaction finishes, another transaction updates the ingredients for that same pizza.

### Case 3: Phantom Read

The meal planner exposes the endpoint GET /calendar/{date}/total_nutrition, which calculates the total macros for all pizzas scheduled on a specific day. A phantom read could occur if the transaction begins by querying all calendar entries for that date and collecting the (pizzaId, quantity) pairs needed for the nutrition calculation. While this transaction is still processing, another transaction could execute POST /calendar/2026-04-21/pizzas and insert a new pizza entry for that same date.
