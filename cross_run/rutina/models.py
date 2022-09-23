from math import fabs
from django.db import models

# Create your models here.
class Ejercicio (models.Model):
    nombre = models.CharField(max_length=100)
#    id_categoria = models.ForeignKey(Categoria)


class Categoria (models.Model):
    id_ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)


class Rutina (models.Model):
    id_categoria = models.ForeignKey(Categoria, null=False, on_delete=models.CASCADE)
    id_ejercicio = models.ForeignKey(Ejercicio, null=False, on_delete=models.CASCADE)
    cantidadMax = models.IntegerField(default=None)
    cantidadMin = models.IntegerField(default=None)

