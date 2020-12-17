from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog.models import Product
from django.contrib.auth.models import User

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


    class Meta:
        verbose_name = "Favoris"