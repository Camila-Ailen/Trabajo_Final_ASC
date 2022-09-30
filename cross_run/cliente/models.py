from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre', default=None)
    apellido = models.CharField(max_length=100, verbose_name='Apellido', default=None)
    numTelefono = models.CharField(max_length=30, verbose_name='Numero de telefono', default=None)
    email = models.CharField(max_length=100, verbose_name='Email', default=None)
    estado = models.BooleanField(default=True, verbose_name='Estado')
    estaEnDeuda = models.BooleanField(default=False, verbose_name='Deuda')

    def __str__(self):
        return self.nombre  