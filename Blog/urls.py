from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from Blog.views import *

urlpatterns = [
    path('', post_list, name = 'inicio'),    
    path('about/', about, name = 'about' ),
    path('pages/', pages, name = 'pages' ),

    path('posts/', post_list, name='post_list'),
    path('postcreate/', post_create, name='post_create'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('posts/<int:pk>/update/', post_update, name='post_update'),
    path('posts/<int:pk>/delete/', post_delete, name='post_delete'),
    
    
    path('Users/', include('Users.urls')),

    path('summernote/', include('django_summernote.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)