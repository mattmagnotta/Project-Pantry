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


def ingredients(request):
    ingredients = Ingredient.objects.all()
    quantity = Ingredient.objects.all()
    price = Ingredient.objects.all()
    print(ingredients)
    context = {
        'ingredients': ingredients,
        'quantity': quantity,
        'price': price,
    }
    return render(request, 'pantryapp/ingredients.html', context)



def save_ingredient(request):
    print(request.POST)
    ingredient_name = request.POST['ingredient_name']
    print('*'*100)
    print(ingredient_name)
    print('*'*100)
    # use requests to ask api for the ingredient price
    price_request = requests.get('https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples')
    print(price_request)
    ingredient = Ingredient(name=ingredient_name, user=request.user)
    ingredient.save()
    return HttpResponseRedirect(reverse('pantryapp:ingredients'))
