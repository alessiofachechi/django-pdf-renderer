from django.db import models

# Create your models here.
from django.db.models import Model


class Product(Model):
    name = models.CharField(max_length=100)
