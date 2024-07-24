from django.db import models

# Create your models here.

class Configuracion(models.Model):
    nombre = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre 
