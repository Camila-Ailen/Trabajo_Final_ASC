from django.db import models
from cliente.models import Cliente

# Create your models here.
class Turno(models.Model):
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    precio = models.DecimalField(decimal_places=2, max_digits=5)
    cuotaClientesMaximo = models.PositiveIntegerField()
    cuotaClientesMinimo = models.PositiveIntegerField()


class TurnoTemporal(models.Model):
    id_turno = models.ForeignKey(Turno, null=False, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, null=False, on_delete=models.CASCADE)
    fechaHoy = models.DateField()