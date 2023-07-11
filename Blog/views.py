from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from Blog.models import *
""" from Blog.forms import * """
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def inicio(request):
    return render(request, 'index.html')