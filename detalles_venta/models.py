from django.db import models
from ventas.models import Venta
from articles.models import Article
from django.core.exceptions import ValidationError
from decimal import Decimal
class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles',null=True, blank=True)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
    # Solo verifica si venta está presente cuando sea necesario y ya esté asignada
        if not self.venta:
            raise ValidationError({'venta': "La venta es requerida."})
        if self.cantidad <= 0:
            raise ValidationError({'cantidad': "La cantidad debe ser un número positivo."})
        if self.precio_unitario <= Decimal('0'):
            raise ValidationError({'precio_unitario': "El precio unitario debe ser un número positivo."})


    def save(self, *args, **kwargs):
        self.total = Decimal(self.cantidad) * self.precio_unitario
        self.full_clean()
        super().save(*args, **kwargs)