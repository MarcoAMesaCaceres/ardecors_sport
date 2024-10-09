from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class DetalleCompra(models.Model):
    id = models.AutoField(primary_key=True)
    compra = models.ForeignKey(
    'compras.Compras',
    on_delete=models.CASCADE,
    related_name='detalles',
    null=True  # Agrega esto
    )
    insumo = models.ForeignKey(
    'insumos.Insumos',
    on_delete=models.PROTECT,
    related_name='detalles_compra',
    null=True  # Agrega esto
    )
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def clean(self):
        if self.cantidad <= 0:
            raise ValidationError({'cantidad': "La cantidad debe ser mayor que cero."})
        if self.insumo:
            # Obtener el stock actual del insumo
            stock_actual = self.insumo.stock
            if self.cantidad > stock_actual:
                raise ValidationError({
                    'cantidad': f"No hay suficiente stock. Disponible: {stock_actual}"
                })

    def save(self, *args, **kwargs):
        if not self.precio_unitario and self.insumo:
            self.precio_unitario = self.insumo.precio
        self.total = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)
        if self.compra:
            self.compra.actualizar_total()

    def __str__(self):
        return f"Detalle compra {self.id} - {self.insumo.nombre if self.insumo else 'N/A'}"

    class Meta:
        verbose_name = "Detalle de Compra"
        verbose_name_plural = "Detalles de Compra"