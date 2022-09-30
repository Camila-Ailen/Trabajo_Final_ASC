from django.db import models

# Create your models here.
class Ejercicio (models.Model):
    nombre = models.CharField(max_length=100, null=False),


class Categoria (models.Model):
    nombre = models.CharField(max_length=100, null=False),



class Rutina(models.Model):
    cantidadMax = models.IntegerField(default=10),
    cantidadMin = models.IntegerField(default=2),