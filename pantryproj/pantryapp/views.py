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

# ingredients table
@login_required
def ingredients(request):
    ingredients = request.user.ingredients.all()
    context = {
        'ingredients': ingredients
    }
    return render(request, 'pantryapp/ingredients.html', context)



        # favorited_recipes_ids.append(recipe.spoonacular_recipe_id)
    # print(favorited_recipes_ids)

# saves the ingredient to the database
def save_ingredient(request):
    print(request.POST)
    ingredient_name = request.POST['ingredient_name']
    ingredient_quantity = request.POST['ingredient_quantity']
    ingredient = Ingredient(name=ingredient_name, quantity=ingredient_quantity, user=request.user)
    ingredient.save()
    return HttpResponseRedirect(reverse('pantryapp:ingredients'))


# clears the ingredient table
def clear_table(request):
    ingredients = request.user.ingredients.all()
    ingredients.delete()
    return HttpResponseRedirect(reverse('pantryapp:ingredients'))



# gets the recipes when the make recipe button is clicked
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
    print(recipes[0]['id'])
    for recipe in recipes:
        if Recipe.objects.filter(user=request.user, spoonacular_recipe_id=recipe['id']).first():
            recipe['favorited'] = True
        else:
            recipe['favorited'] = False
    context = {
        'recipes' : recipes,

    }
    return render(request, 'pantryapp/recipe.html', context)


# creates the cards with image recipes
def make_recipes(request, recipe_id):
    url = 'https://api.spoonacular.com/recipes/' + str(recipe_id)  + '/information/?apiKey=' + spoonacular_api_key
    response = requests.get(url)
    recipe_information = json.loads(response.text)

    context = {
        'recipe': recipe_information,
    }

    return render(request, 'pantryapp/make_recipes.html', context)




# gets the json from spoonacular using recipe id
def favorite_recipe(request):
    data = json.loads(request.body)
    # print(data)
    user = request.user
    id = data['recipe_id']
    title = data['recipe_title']
    image = data['recipe_image']
    recipe = Recipe.objects.filter(user=user, spoonacular_recipe_id=id).first()
    print(recipe)
    if recipe is None:
        # recipe = Recipe(user=user, spoonacular_recipe_id=id,recipe_image=image, recipe_title=title)
        recipe = Recipe(user=user, spoonacular_recipe_id=id, title=title, image=image)
        recipe.save()
    else:
        recipe.delete()
        

    return HttpResponse('ok')


# displays the users saved recipes
@login_required
def saved_recipes(request):
    # db_recipes = request.user.recipes.all()
    # # favorited_recipes_ids = []
    # recipes = [] # pass to the template
    # for recipe in db_recipes:
    #     recipe_id = recipe.spoonacular_recipe_id
    #     url = 'https://api.spoonacular.com/recipes/' + str(recipe_id)  + '/information/?apiKey=' + spoonacular_api_key
    #     response = requests.get(url)
    #     recipe_information = json.loads(response.text)
    #     recipes.append(recipe_information)
    recipes = request.user.recipes.all()
    # for recipe in recipes:
    #     if Recipe.objects.filter(user=request.user, spoonacular_recipe_id=recipe['id']).first():
    #         recipe['favorited'] = True
    #     else:
    #         recipe['favorited'] = False
    context = {
        'recipes' : recipes
    }
    return render(request, 'pantryapp/saved_recipes.html', context)
        # recipes = Recipe.objects.all()
        # context = {
        #     'recipes': recipes
        # }
        # return render(request, 'pantryapp/saved_recipes.html', context)
# unsaves a recipes
def unfavorite_recipe(request,):
    user = request.user
    recipe = Recipe.objects.filter(user=user, spoonacular_recipe_id=id).first()
    print(recipe)
    recipe.delete()

    return HttpResponse('ok')
