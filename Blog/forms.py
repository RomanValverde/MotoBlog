from django import forms
from .models import Post
from datetime import date
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    subtitulo = forms.CharField(max_length=200)
    cuerpo = forms.CharField(widget=SummernoteWidget())
    imagen = forms.ImageField(required=False)
