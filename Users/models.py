from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

def user_avatar_path(instance, filename):
    # Obtiene el nombre de usuario del perfil
    username = instance.user.username
    # Obtiene la extensión del archivo
    ext = filename.split('.')[-1]
    # Genera el nombre único del archivo combinando el nombre de usuario y la extensión
    unique_filename = f"{username}.{ext}"
    # Genera la ruta completa del archivo dentro de la carpeta del usuario
    folder_path = f"avatars/{username}"
    return os.path.join(folder_path, unique_filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=user_avatar_path, blank=True)
    description = models.TextField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
