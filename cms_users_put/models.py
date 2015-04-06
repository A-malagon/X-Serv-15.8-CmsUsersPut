from django.db import models

# Create your models here.

class PrecioCoches(models.Model):
    marca = models.CharField(max_length=32)
    modelo = models.CharField(max_length=32)
    precio = models.PositiveIntegerField()
