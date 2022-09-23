from django.db import models
from cliente.models import Cliente

# Create your models here.
class TipoPago(models.Model):
    detalle = models.CharField(max_length=100)


class Pago(models.Model):
    id_tipoPago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fechaYHora = models.DateTimeField(auto_now_add=True)
    montoDePago = models.DecimalField(decimal_places=2, max_digits=5)
    nroComprobante = models.PositiveIntegerField(null=True)





