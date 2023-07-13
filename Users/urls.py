from django.urls import path, include
from Users.views import *

urlpatterns = [
    
    path('login/', myLogin, name = 'myLogin'),
    path('logout/', myLogout, name = 'myLogout'),
    path('register/', myRegistry, name = 'myRegistry'),

]    