from django.shortcuts import render,reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Recipe, Ingredient
import requests



# ?apiKey=YOUR-API-KEY.
def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'pantryapp/index.html', context)


# @login_required
def ingredients(request):
    # ingredients = Ingredient.objects.all()
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
    print('*'*100)
    print(ingredient_name)
    print('*'*100)
    # use requests to ask api for the ingredient price
    price_request = requests.get('https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples')
    print(price_request)
    ingredient = Ingredient(name=ingredient_name, quantity=ingredient_quantity, user=request.user)
    ingredient.save()
    return HttpResponseRedirect(reverse('pantryapp:ingredients'))
