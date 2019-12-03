from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    spoonacular_recipe_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)


    def __str__(self):
        return self.spoonacular_recipe_id

class Ingredient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name




# recipes view
#     take the logged in user, find all their ingredients
#     put the ingedients into the url for the request
#     send the request, get the response
#     pass the response data to the template to be rendered
# save a recipe





# ingredient = Ingredient.objects.get(id=1)
# print(ingredient.user.username)
#
# user = User.objects.get(id=1)
# user.ingredients.all()
#
#
#
# User
# | id | username |
# | 1  | admin    |
# | 2  | someguy  |
#
#
# Ingredients
# | id | name       | user_id |
# | 1  | carrots    | 1       |
# | 2  | tomato     | 1       |
# | 3  | soup       | 1       |
# | 4  | carrots    | 2       |
