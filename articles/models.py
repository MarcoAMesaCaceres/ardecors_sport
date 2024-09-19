from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

from django.core.validators import RegexValidator, MinValueValidator

class Article(models.Model):
    nombre = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s]+$',
                message='El nombre solo puede contener letras (incluyendo tildes), números y espacios.'
            )
        ]
    )
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01, message='El precio debe ser un número positivo.')
        ]
    )
    stock = models.IntegerField(
        validators=[
            MinValueValidator(0, message='El stock debe ser un número positivo o cero.')
        ]
    )
    imagen = models.ImageField(upload_to='articulos/', null=True, blank=True)

    def __str__(self):
        return self.nombre