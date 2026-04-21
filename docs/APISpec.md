# API Specification

### Pizzas

* Add Recipe(WRITE FUNCTION)
  (POST /pizzas)

  Input: 
  {
    "name": "string",
    "ingredients": [
      {
        "ingredientId": "integer",
        "amount": "number"
      }
    ]
  }
  
  Output: 
  {
    "pizzaId": "integer"
  }


* As a gym-goer, I want a system to automatically calculate and display the nutritional information of my custom pizza, so that I can understand how my ingredient choices impact calories, fats, protein, and other nutrients.

* As a frequent user, I want to save and favorite my best pizza recipes, so that I can easily revisit and remake them later.

* As a chef, I want to track the current pizza ingredients in my kitchen so I know what I can and can’t make, as well as what I might need to buy more of.

* As a dietician, I want to add tags to my pizza recipes so I can track certain information about them (e.g. vegan, gluten free, etc.)

* As a dieter, I want to track my pizzas and when I’ve eaten them so I can holistically monitor my eating habits and health.

* As a foodie, I want to share my recipes with others, so that I can get feedback on what to improve or what to try

* As an allergist, I want to find safe ingredient substitutes for common allergens, so that my clients can still enjoy pizza while adhering to their medical and allergic needs.

* As a student, I want to find the cheapest and most filling toppings, so that I can budget while still having the ability to enjoy my pizza.

* As a traveler, I want to be able to sort by popularity so that I will able to try all sorts of unique pizzas (like pineapple or kiwi on pizza)

* As an impoverished person, I want to sort by what appliances are necessary so I want to be able to determine which pizzas I can make with resources

* As a parent with very limited time, I want to sort by time needed to make recipes so I can make a quick meal for my family





### Ingredients

* Exception: Unknown Ingredient

    If a user decides to use an ingredient that is unavailable, we will display a message and give the user the option to add a new recipe. 

* Exception: Missing nutritional data

    If an ingredient doesn't have nutritional information, we will notify the user and give them the option to either remove the ingredient or provide them with a rough estimate.

* Exception:  Duplicate favorites
  
    If a user saves a recipe that is already favorited, we will notify them that it is already saved. 

* Exception: Duplicate ingredients

    If a new ingredient is added to the kitchen ingredients table that is already in there, it should notify the user the ingredient already exists and not add it.

* Exception: Duplicate tags

    If a user tries to make a tag that already exists, it should notify them that the tag already exists and not create a new one

* Exception: Duplicate entries 

    If a pizza is added on the same day and that same type of pizza was already eaten that day, it should increment a quantity rather than make a new entry.

* Exception: Failed to Share

    If a user attempts to share a recipe but the request fails due to a poor connection to the network, the system will notify the user of the poor connection and allow them to resubmit the share request.

* Exception: Allergen Detected in Recipe

    If a user creates a recipe or views a recipe that contains a known allergen of the user, the system will display a clear warning, highlight the allergen within the recipe, and suggest safe alternatives.

* Exception: Total Cost Exceeds Budget

    If a user creates a recipe that exceeds their set budget, the system will display a reminder of their budget and how much they’re over. Additionally, it will offer alternatives that cut down the cost the most, so that it fits the budget.

* Exception: Missing Rating

    If a recipe is sorted that is unrated, it will automatically be sorted in the middle with around ⅗ stars as the assumed rating

* Exception: Unlisted Appliances

    If a recipe doesn’t list what appliances are required, then we will automatically sort them with the more intensive recipes (such as those that require a stove or a food processor) 

* Exception: Missing Time

    If a recipe is posted without an estimated time then we will automatically sort them at the highest time required when sorting from lowest to highest time
