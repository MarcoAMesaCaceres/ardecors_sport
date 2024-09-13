from django.db import models
from django.core.exceptions import ValidationError
import datetime

class DetalleCompra(models.Model):
    id = models.AutoField(primary_key=True)
    compra = models.ForeignKey('compras.Compras', on_delete=models.CASCADE, related_name='detalles',null=True)
    producto = models.CharField(max_length=255,null=True)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def clean(self):
        if self.cantidad <= 0:
            raise ValidationError({'cantidad': "La cantidad debe ser mayor que cero."})
        if self.precio_unitario <= 0:
            raise ValidationError({'precio_unitario': "El precio unitario debe ser mayor que cero."})

    def save(self, *args, **kwargs):
        self.full_clean()
        self.total = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Detalle de compra {self.id} - {self.producto} - Orden {self.compra.id}"