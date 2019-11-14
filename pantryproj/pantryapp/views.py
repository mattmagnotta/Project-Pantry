from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

# def index(request):
#     context = {
#         'message': 'Hello World!'
#     }
#     return render(request, 'pantryapp/index.html', context)


def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'pantryapp/index.html', context)
