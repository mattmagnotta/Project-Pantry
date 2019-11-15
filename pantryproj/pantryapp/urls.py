from django.urls import path
from . import views

app_name = 'pantryapp'
urlpatterns = [
  path('', views.index, name='index'),
  path('ingredients/', views.ingredients, name='ingredients'),
  path('save_ingredient/', views.ingredents_tool, name='save_ingredient'),
]
