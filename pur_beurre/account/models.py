from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog.models import Product
from django.contrib.auth.models import User

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    base_product = models.ManyToManyField(Product, related_name='Produit', blank=True)
    substitute = models.ManyToManyField(Product, related_name='Substitution', blank=True)

    class Meta:
        verbose_name = "Favoris"