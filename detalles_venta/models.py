from django.db import models
from ventas.models import Venta
from articles.models import Article
from django.core.exceptions import ValidationError
from decimal import Decimal
class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles',null=True, blank=True)
    articulo = models.ForeignKey(Article, on_delete=models.CASCADE,null=True, blank=True)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if not self.venta:
            raise ValidationError({'venta': "La venta es requerida."})
        if not self.articulo:
            raise ValidationError({'articulo': "El artículo es requerido."})
        if self.cantidad <= 0:
            raise ValidationError({'cantidad': "La cantidad debe ser un número positivo."})
        if self.precio_unitario <= Decimal('0'):
            raise ValidationError({'precio_unitario': "El precio unitario debe ser un número positivo."})
        if self.articulo and self.articulo.stock < self.cantidad:
            raise ValidationError({'cantidad': f"No hay suficiente stock para este artículo. Stock disponible: {self.articulo.stock}"})

    def save(self, *args, **kwargs):
        self.total = Decimal(self.cantidad) * self.precio_unitario
        self.full_clean()
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.total = Decimal(self.cantidad) * self.precio_unitario
        self.full_clean()
        super().save(*args, **kwargs)