from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from Users.models import *
from Users.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate , update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def myLogin(request):
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/../')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
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

@login_required
def myProfile(request):
    user = request.user

    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('myProfile')
    else:
        form = UserUpdateForm(instance=user)

    context = {'form': form}
    return render(request, 'profile.html', context)

def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('myProfile')
    else:
        form = PasswordChangeForm(request.user)
    
    context = {'form': form}
    return render(request, 'changePassword.html', context)





