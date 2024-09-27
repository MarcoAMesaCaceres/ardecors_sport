from django.db import models
from django.core.exceptions import ValidationError
import datetime
from insumos.models import Insumos
class DetalleCompra(models.Model):
    id = models.AutoField(primary_key=True)
    compra = models.ForeignKey('compras.Compras', on_delete=models.CASCADE, related_name='detalles', null=True)
    insumo = models.ForeignKey(Insumos, on_delete=models.SET_NULL, null=True)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    def clean(self):
        if self.cantidad <= 0:
            raise ValidationError({'cantidad': "La cantidad debe ser mayor que cero."})
        if self.insumo and self.cantidad > self.insumo.stock:
            raise ValidationError({'cantidad': f"La cantidad no puede ser mayor que el stock disponible ({self.insumo.stock})."})

    def save(self, *args, **kwargs):
        self.full_clean()
        if self.insumo:
            self.precio_unitario = self.insumo.precio
        self.total = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Detalle de compra {self.id} - {self.insumo.nombre if self.insumo else 'N/A'} - Orden {self.compra.id}"