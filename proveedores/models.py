from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import RegexValidator, EmailValidator


class Proveedor(models.Model):
    nombre = models.CharField(
        max_length=255, 
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='El nombre solo puede contener letras y espacios.',
            ),
        ]
    )
    contacto = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(
        max_length=13, 
        blank=True, 
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+57[3][0-9]{9}$',
                message='El número de teléfono debe tener el formato +57 seguido de 10 dígitos.',
            ),
        ]
    )
    email = models.EmailField(blank=True, null=True, validators=[EmailValidator()])
    direccion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.nombre

    def clean(self):
        super().clean()
        if not self.email and not self.telefono:
            raise ValidationError('Se debe proporcionar al menos un email o un número de teléfono.')

    def delete(self, *args, **kwargs):
        # Verificar si tiene insumos asociados
        if self.insumos_set.exists():
            raise ValidationError("No se puede eliminar el proveedor porque tiene insumos asociados.")
        super().delete(*args, **kwargs)
