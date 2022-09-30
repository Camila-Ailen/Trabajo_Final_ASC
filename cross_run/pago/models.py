from django.db import models
from cliente.models import Cliente

# Create your models here.
class TipoPago(models.Model):
    detalle = models.CharField(max_length=100),


class Tipo(models.Model):
    id_tipo_pago = models.ForeignKey(TipoPago, on_delete= models.CASCADE),
    id_Cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE),
    fechaYHora = models.DateTimeField(auto_now_add=True, null=True),
    montoDePago = models.DecimalField(max_digits=6, decimal_places=2, null=True),
    nroComprobante= models.IntegerField(null=True),