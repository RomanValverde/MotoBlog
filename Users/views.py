from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from Users.models import *
from Users.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def myLogin(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['user'], password = request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect('/../')
        else:
            return render(request, 'login.html', {'error': 'Usuario o Contraseña incorrectos'})
    else:
        return render(request, 'login.html')

def myRegistry(request):
    if request.method == "POST":
        userCreate = CustomUserCreationForm(request.POST)
        if userCreate.is_valid():
            userCreate.save()
            return redirect('../login')
    else:
        userCreate = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': userCreate})

def myLogout(request):
    logout(request)
    return redirect('/../')


