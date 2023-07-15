from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    description = models.TextField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
