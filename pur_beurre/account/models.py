from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog.models import Product

class User(AbstractUser):
    pass
    """first_name = models.CharField("Prénom", max_length=100)
    last_name = models.CharField("Nom", max_length=50)
    password = models.CharField("Mot de passe", max_length=50)
    email = models.EmailField("E-mail", max_length=200, unique=True)"""

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    base_product = models.ManyToManyField(Product, related_name='Produit', blank=True)
    substitute = models.ManyToManyField(Product, related_name='Substitution', blank=True)

    class Meta:
        verbose_name = "Favoris"