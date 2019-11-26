from django.urls import path
from . import views

app_name = 'pantryapp'
urlpatterns = [
  path('', views.index, name='index'),
  path('ingredients/', views.ingredients, name='ingredients'),
  path('save_ingredient/', views.save_ingredient, name='save_ingredient'),
  path('clear_table/', views.clear_table, name='clear_table'),
  path('get_recipes/', views.get_recipes, name='get_recipes'),
  path('saved_recipes/', views.saved_recipes, name='saved_recipes'),
  path('make_recipes/<int:recipe_id>/', views.make_recipes, name='make_recipes'),
  path('favorite_recipe/<int:recipe_id>/', views.favorite_recipe, name='favorite_recipe'),
  path('unfavorite_recipe/int:recipe_id>/', views.unfavorite_recipe, name='unfavorite_recipe')

]
