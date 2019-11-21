from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_page(request):
    return render(request, 'userapp/index.html')

def registration_page(request):
    return render(request,'userapp/register.html')

def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)

    return HttpResponseRedirect(reverse('pantryapp:index'))

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None: # username and password matched a user
        login(request, user)
        return HttpResponseRedirect(reverse('pantryapp:index'))
    else:
        return HttpResponseRedirect(reverse('userapp:login_register'))



def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('pantryapp:index'))
