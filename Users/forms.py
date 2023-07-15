from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    avatar = forms.ImageField(required=False)
    description = forms.CharField(required=False)
    website = forms.URLField(required=False)
    dateOfBirth = forms.DateField(widget=SelectDateWidget(years=range(1920, 2100)),required=False)
    country = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar', 'description', 'dateOfBirth', 'country']

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'customInput'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'customInput'}))
