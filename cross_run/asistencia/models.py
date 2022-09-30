from django.db import models
from cliente.models import Cliente
from turno.models import Turno

# Create your models here.
class Asistencia (models.Model):
    id_turno = models.ForeignKey(Turno, on_delete = models.CASCADE),
    id_cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE),
    fechaYHora = models.DateTimeField(auto_now_add=True)