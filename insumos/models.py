from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from proveedores.models import Proveedor
from django.core.exceptions import ValidationError
from detalles_compra.models import DetalleCompra

class Insumos(models.Model):
    id = models.AutoField(primary_key=True)
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
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    stock = models.IntegerField(
        validators=[
            MinValueValidator(0, message='El stock debe ser un número positivo o cero.')
        ]
    )

    def __str__(self):
        return self.nombre

    def delete(self, *args, **kwargs):
        # Verificar si tiene compras asociadas
        if DetalleCompra.objects.filter(insumo=self).exists():
            raise ValidationError("No se puede eliminar el insumo porque tiene compras asociadas.")
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"