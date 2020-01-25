# Project-Pantry
An ingredient tracking application


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


#### Mealplanning
Although this is a milestone type 3, I would like to tap into the database and offer customized meal plans or allow the user build their own using the interactive meal planning tool to schedule meals for each day of the week.



# Functionality

You will arrive at the landing page. The landing page will be simple and clean. It will have a login/register feature on the landing page.

Once you login in you will be redirected to the users homepage. The homepage will consist of, a side nav, a randomly generated carousel of random recipes of the day, and a 'just for you section'. The 'just for you section' will contain your log of recipe collections, meal plans, and a food journal.

The side nav will be a flyout nav. Once a user clicks the hamburger button the side nav will slide out. Starting from the top of the nav and moving downwards, the nav will have a link to go to the users feed(home), a link to plan and shop, and a link to run the inventory tool. Then the majority of the nav will be made up of saved recipes and user collections. (e.g) a folder for breakfeast, a folder for lunches, and a folder for dinners.

When you click on "collection folder", you can select recipes. When a recipe is selected it will go to a view that renders a price breakdown of each ingredient graph and a nutritional data for each ingredient graph. This view will also show the user which ingredients they need to purchase in order to make the recipe.

# Data model

Pantry will use a user model, a recipe model, and an ingredient model.

The user model will store a first & last name , username, email address, and password.

The recipe model will store an id, recipe name, recipe ingredients, recipe link.

the ingredients model will store, id, name , a boolean value for having the ingredient or having to buy it.

# Schedule

#### Week 1
I would like to have the general layout of the page done. I want to begin building on the nav during this phase.

#### Week 2
During this phase I hope to start stitching together all the pieces to make web page. I want the nav bar to be functioning by the end of this phase.

#### Week 3
The final phase ... I hope to work out all the bugs and tweak final design during this phase. I would like to have the inventory tool working and completed, as thats the meat and potatoes of the web application.

#### After the dust settles
I hope to add the meal planning feature to allow the users to log recipes for certain days of the week. 
