from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100),
    apellido = models.CharField(max_length=100),
    numTelefono = models.CharField(max_length=30),
    email = models.CharField(max_length=100),
    estado = models.BooleanField(default=True),
    estaEnDeuda = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre  