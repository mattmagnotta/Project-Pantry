from django.db import models
from django.contrib.auth.models import User
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spoonacular_recipe_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name
