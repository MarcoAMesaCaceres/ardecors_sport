from django.db import models
from ventas.models import Venta
from articles.models import Article

class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey('ventas.Venta', on_delete=models.CASCADE, related_name='detalles', to_field='id', null=True)
    articulo = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle de Venta {self.id} - Venta {self.venta.id}"

    def save(self, *args, **kwargs):
        self.total = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)