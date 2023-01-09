from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class user(models.Model):
    username=models.CharField(max_length=50)
    emailname=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)

    def __str__(self):
            return self.username

class userAvatar(models.Model):
    imagen=models.ImageField(upload_to='avatares')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} - {self.imagen}"

