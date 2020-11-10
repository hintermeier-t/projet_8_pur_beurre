from django.db import models

from django.db import models
from products.model import Product

class User(models.Model):
    first_name = models.CharField("Prénom", max_length=100)
    last_name = models.CharField("Nom", max_length=50)
    password = models.CharField("Mot de passe", max_length=50)
    email = models.EmailField("E-mail", max_length=200, unique = True)

class UserSubstitute(model.Model):
    user = models.ManyToManyField(User, related_name="Utilisateur", blank=True)
    base_product = models.ManyToManyField(Product, related_name="Produit de base", blank=True)
    substitute = models.ManyToManyField(Product, related_name="Produit de substitution", blank=True)