# Project-Pantry
An ingredient tracking application


## Project Overview
### Pantry use cases:
#### Whats in my fridge
Find recipes that use as many of the
ingredients you have available while limiting missing
ingredients. This feature will also store users ingredients into a running log.

**What should I make**
Get a list of recipes using a special
ingredient (or several ingredients) that
you want to turn into something
delicious.
Get inspired with the seasonal produce
you found at the farmers’ market or find
the perfect chocolate-cherry-walnut
dessert.


#### Mealplanning
Although this is a milestone type 3, I would like to tap into the database and offer customized meal plans or allow the user build their own using the interactive meal planning tool



# Functionality

You will arrive at the landing page. The landing page will be simple and clean. It will have a login/register feature on the landing page.

Once you login in you will be redirected to the users homepage. The homepage will consist of, a side nav, a randomly generated carousel of images of food, and a 'just for you section'.

The side nav will be a flyout nav. Once a user clicks the hamburger button the side nav will slide out. Starting from the top of the nav and moving downwards, the nav will have a link to go to the users feed, a link to plan and shop, and a link to run the inventory. Then the majority of the nav will be made up of saved recipes and user collections. (e.g) a folder for breakfeast, a folder for lunches, and a folder for dinners.

When you click on "collection folder", you can select recipes. When a recipe is selected it will go to a view that renders a price breakdown graph and a nutritional data graph. This view will also show the user which ingredients they need to purchase.

# Data model

Pantry will use a user model, a recipe model, and an ingredient model.

![Alt text](/code/projects/capstone/user_table.jpg?raw=true "Optional Title")
