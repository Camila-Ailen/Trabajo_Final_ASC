from tkinter import CASCADE
from django.db import models
from cliente.models import Cliente
from datetime import datetime


# Create your models here.



class Turno (models.Model):
    cliente = models.ManyToManyField(Cliente)
    horaInicio = models.TimeField(default=None)
    horaFin = models.TimeField(default=None)
    precio = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    cuotaClienteMax = models.IntegerField(default=0, null=True)
    cuotaClienteMin = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.id_turno


'''
class TurnoTemporal(models.Model):
    id_turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fechaHoy = models.DateTimeField()

    def __str__(self):
        return self.fechaHoy

'''