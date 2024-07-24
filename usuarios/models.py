from django.db import models

# Create your models here.

class Usuarios(models.Model):
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    tipo_documento = models.CharField(max_length=20)
    documento = models.CharField(max_length=20, unique=True)
    correo = models.EmailField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido}"