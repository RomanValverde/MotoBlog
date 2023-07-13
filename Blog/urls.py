from django.urls import path, include
from Blog.views import *

urlpatterns = [
    path('', inicio, name = 'inicio'),    
    path('Users/', include('Users.urls')),

]    