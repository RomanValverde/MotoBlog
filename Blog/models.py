from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='deleted-user')
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='post_images/')

    def __str__(self):
        return self.titulo