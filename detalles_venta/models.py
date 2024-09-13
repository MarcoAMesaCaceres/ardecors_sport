from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from ventas.models import Venta
from articles.models import Article

class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles',null=True)
    articulo = models.ForeignKey(Article, on_delete=models.CASCADE,null=True)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if self.cantidad <= 0:
            raise ValidationError({'cantidad': "La cantidad debe ser mayor que cero."})
        
        if self.articulo and self.articulo.stock < self.cantidad:
            raise ValidationError({'cantidad': "No hay stock suficiente para este artículo."})

    def save(self, *args, **kwargs):
        self.total = self.cantidad * self.precio_unitario
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Detalle de Venta {self.id} - Venta {self.venta.id}"