from django.urls import path
from . import views

app_name = 'pantryapp'
urlpatterns = [
  path('', views.index, name='index'),
  path('ingredients/', views.ingredients, name='ingredients'),
  path('save_ingredient/', views.save_ingredient, name='save_ingredient'),
  path('clear_table/', views.clear_table, name='clear_table'),
  path('get_recipes/', views.get_recipes, name='get_recipes'),
  ]
