from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError

class Clientes(models.Model):
    documento = models.CharField(
        max_length=20, 
        unique=True, 
        null=True,  # Allow null temporarily
        blank=True,  # Allow blank temporarily
        validators=[
            RegexValidator(
                regex=r'^\d{8,10}$',
                message='El número de documento debe tener entre 8 y 10 dígitos.',
            ),
        ]
    )
    nombre = models.CharField(max_length=255, validators=[
        RegexValidator(
            regex=r'^[a-zA-ZñÑ\s]+$',
            message='El nombre solo puede contener letras y espacios.',
        ),
    ])
    contacto = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=13, blank=True, null=True, validators=[
        RegexValidator(
            regex=r'^\+57[3][0-9]{9}$',
            message='El número de teléfono debe tener el formato +57 seguido de 10 dígitos.',
        ),
    ])
    email = models.EmailField(blank=True, null=True, validators=[EmailValidator()])
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.documento or 'Sin documento'}"

    def clean(self):
        super().clean()
        if not self.email and not self.telefono:
            raise ValidationError('Se debe proporcionar al menos un email o un número de teléfono.')

    def tiene_ventas(self):
        return self.ventas.exists()