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
