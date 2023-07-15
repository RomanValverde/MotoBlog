from django.urls import path, include
from Users.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('login/', myLogin, name = 'myLogin'),
    path('logout/', myLogout, name = 'myLogout'),
    path('register/', myRegistry, name = 'myRegistry'),
    path('profile/', myProfile, name = 'myProfile'),
    path('profile/changePassword', changePassword, name = 'changePassword'),
    path('profile/deleteUser', deleteUser, name = 'deleteUser'),
    path('profile/deleteAvatar', deleteAvatar, name ='deleteAvatar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
