# Project-Pantry
An ingredient tracking web-application


## Project Overview
### Pantry use cases:
#### Whats in my fridge
Find recipes that use as many of the
ingredients you have available while limiting missing
ingredients. This feature will also store users ingredients into a running log.

#### What should I make
Get a list of recipes using a special
ingredient (or several ingredients) that
you want to turn into something
delicious.
Get inspired with the seasonal produce
you found at the farmers’ market or find
the perfect chocolate-cherry-walnut
dessert.


# Functionality
Pantry uses Python and Django on the backend, HTML/CSS, JavaScript, & Materialize on the frontend.
When you arrive at the landing page you will be met with a parallax with some information about the app.
![](screenshots/landing_page.png)




 From here you can either create an account or login, I used Djangos user system to make this happen. After you have logged in you will then be able to navigate to a 'My Ingredients' tab. Once there you are now able to inventory the ingredients you have on hand OR that you want to use.
 ![](screenshots/ingredients.png)


After you finish adding the ingredients, you can click the get recipes button, once that is clicked it makes a call to the Spoonacular API. You will then be routed to a page consisting of cards with an image of the recipe, a button to make the recipe, and a button to save the recipe.
 ![](screenshots/get_recipes.png)


Once you find the recipe of your choice, you can click the make recipe to be routed to a page consisting of ingredients and instructions on how to make that recipe. It also has a button for 'more information', when clicked, it will take you to the website where the original recipe was posted. It will also show you if you already have a recipe saved or not.
 ![](screenshots/make_recipes.png)


Pantry allows you to save recipes to your 'My Recipes' view. This view also consists of cards, they are sorted by most recent.
 ![](screenshots/my_recipes.png)





# Data model

Pantry will use a user model, a recipe model, and an ingredient model.

The user model will store a first & last name , username, email address, and password.

The recipe model will store an id, recipe name, recipe ingredients, recipe link.

the ingredients model will store, id, name , a boolean value for having the ingredient or having to buy it.
