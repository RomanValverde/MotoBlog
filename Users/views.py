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
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        # Crea un nuevo perfil para el usuario
        profile = Profile(user=user)
        profile.save()

    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            # Actualiza los campos del perfil si no están vacíos
            if form.cleaned_data['description']:
                profile.description = form.cleaned_data['description']
            if form.cleaned_data['website']:
                profile.website = form.cleaned_data['website']
            if form.cleaned_data['avatar']:
                profile.avatar = form.cleaned_data['avatar']
            profile.save()
            messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
            return redirect('myProfile')
        else:
            messages.error(request, 'Hubo un error al actualizar tu perfil. Por favor, verifica los datos ingresados.')
    else:
        form = UserUpdateForm(instance=user, initial={
            'description': profile.description,
            'website': profile.website,
            'avatar': profile.avatar
        })

    context = {'form': form, 'profile': profile}
    return render(request, 'profile.html', context)




def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.user
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password1')

            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                return redirect('myProfile')
            else:
                form.add_error('old_password', 'La contraseña actual es incorrecta.')

    else:
        form = PasswordChangeForm(request.user)
    
    context = {'form': form}
    return render(request, 'changePassword.html', context)

@login_required
def deleteUser(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Tu cuenta ha sido eliminada exitosamente.')
        logout(request)
        return redirect('inicio')

    return render(request, 'deleteUser.html')





