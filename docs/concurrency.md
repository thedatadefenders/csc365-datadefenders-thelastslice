## Concurrency Control

### Case 1: Lost Update

Two users each call PUT/pizzas/101 at the same time. Both try to update the pizza by adding ingredients. Without concurrency control, both transactions operate on the same items, each one creating their own version, and one will overwrite the other resulting in one update being lost.

To solve this, we will use pessimistic concurrency control to lock the pizzas table. This doesn't entirely solve the issue of lost updates but will help prevent concurrency issues of changes happening at the same time. For lost updates, we think it's not worth it space-wise to keep a history of every update made to a pizza for a very rare occurence of people updating pizzas at the same time, so we instead update the user_id of the pizza to whoever updated the pizza last so if there are any concurrency issues, it's clear who was the last person to update and who's update got overwritten. 

Sequence diagram: 

![Concurrency Issue 1](/docs/imgs/Concurrency_Issue_1.png)

### Case 2: Concurrency Foreign Key Constraint Violation

POST/history/{pizza_date}/pizzas currently selects from the database to see if the given pizza id exists then inserts a new row into the history using that pizza id. If someone were to delete the pizza with said id inbetween the select and the insert, the insert would fail due to a foreign key constraint violation since the pizza id would no longer exist. To fix this, the select will now also lock the row with the given pizza id, preventing deletion of the pizza id and ensuring the history table insert works without fail.

Sequence diagram:

![Concurrency Issue 2](/docs/imgs/Concurrency_Issue_2.png)

### Case 3: Phantom Read

The meal planner exposes the endpoint GET /history/{date}/total_nutrition, which calculates the total macros for all pizzas scheduled on a specific day. A phantom read could occur if the transaction begins by querying all calendar entries for that date and collecting the (pizzaId, quantity) pairs needed for the nutrition calculation. While this transaction is still processing, another transaction could execute POST /calendar/2026-04-21/pizzas and insert a new pizza entry for that same date.

Sequence diagram:

<img width="829" height="730" alt="image" src="https://github.com/user-attachments/assets/faf6a20d-4cbd-4a00-aad6-4256ad9a47be" />

