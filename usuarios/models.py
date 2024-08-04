from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    usuario = models.CharField(max_length=255, unique=True)
    contrasena = models.CharField(max_length=255)
    ROL_CHOICES = [
        ('Admin', 'Admin'),
        ('Vendedor', 'Vendedor'),
        ('Comprador', 'Comprador'),
    ]
    rol = models.CharField(max_length=10, choices=ROL_CHOICES)

    def __str__(self):
        return self.usuario