from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100, default='', verbose_name='Nombres')
    apellido = models.CharField(max_length=100, default='', verbose_name='Apellido')
    numTelefono = models.CharField(max_length=30, default='', verbose_name='Telefono')
    email = models.CharField(max_length=100, default='', verbose_name='Email')
    estado = models.BooleanField(default=True, verbose_name='Estado Activo')
    estaEnDeuda = models.BooleanField(default=False, verbose_name='Esta en Deuda')

    def __str__(self):
        return 'Nro: {} / Nombres: {}'.format(self.id, self.nombre)

