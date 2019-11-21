from django.shortcuts import render,reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Recipe, Ingredient
import requests
import json
from .secrets import spoonacular_api_key
from django.contrib.auth.decorators import login_required



# ?apiKey=YOUR-API-KEY.
def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'pantryapp/index.html', context)


@login_required
def ingredients(request):
    ingredients = request.user.ingredients.all()
    print(ingredients)
    context = {
        'ingredients': ingredients
    }
    return render(request, 'pantryapp/ingredients.html', context)



def save_ingredient(request):
    print(request.POST)
    ingredient_name = request.POST['ingredient_name']
    ingredient_quantity = request.POST['ingredient_quantity']
    ingredient = Ingredient(name=ingredient_name, quantity=ingredient_quantity, user=request.user)
    ingredient.save()
    return HttpResponseRedirect(reverse('pantryapp:ingredients'))

def clear_table(request):
    ingredients = request.user.ingredients.all()
    ingredients.delete()
    return HttpResponseRedirect(reverse('pantryapp:ingredients'))




@login_required
def get_recipes(request):
    ingredients = request.user.ingredients.all()
    ingredient_params = []
    # loops over the orm to get the instances
    for ingredient in ingredients:
        ingredient_params.append(ingredient.name)

    ingredient_params=','.join(ingredient_params)

    url = 'https://api.spoonacular.com/recipes/findByIngredients?ingredients=' + ingredient_params + ','+ '&number=100' + '&apiKey=' + spoonacular_api_key

    response = requests.get(url)
    # print(response.text)
    recipes = json.loads(response.text)
    # recipes = recipes[10:20]
    for i in range(len(recipes)):
        recipe_id = recipes[i]["id"]
        name = recipes[i]["title"]
        image = recipes[i]["image"]

    context = {
        'recipes' : recipes,
        'recipe_id' : recipe_id,
        'name' : name,
        'image': image,

    }
    return render(request, 'pantryapp/recipe.html', context)
