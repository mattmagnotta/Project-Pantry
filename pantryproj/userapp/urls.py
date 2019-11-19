from django.urls import path
from . import views

app_name = 'userapp'
urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('register/', views.registration_page, name='registration_page'),
    path('register_user/', views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
]
