from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from ventas.models import Venta
from articles.models import Article

class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(
        Venta, 
        on_delete=models.CASCADE,
        related_name='detalles',
        null=True
    )
    articulo = models.ForeignKey(
        Article, 
        on_delete=models.PROTECT,  # Cambiado a PROTECT
        related_name='detalles_venta',
        null=True
        
    )
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def clean(self):
        if self.cantidad <= 0:
            raise ValidationError({'cantidad': "La cantidad debe ser mayor que cero."})
        if self.articulo and self.cantidad > self.articulo.stock:
            raise ValidationError({
                'cantidad': f"No hay suficiente stock. Disponible: {self.articulo.stock}"
            })

    def save(self, *args, **kwargs):
        if not self.precio_unitario:
            self.precio_unitario = self.articulo.precio
        self.total = self.cantidad * self.precio_unitario
        
        # Verificar y actualizar stock
        if self.articulo:
            if not self.pk:  # Si es una nueva venta
                self.articulo.stock -= self.cantidad
            else:  # Si es una actualización
                detalle_antiguo = DetalleVenta.objects.get(pk=self.pk)
                diferencia = self.cantidad - detalle_antiguo.cantidad
                self.articulo.stock -= diferencia
            
            if self.articulo.stock < 0:
                raise ValidationError('No hay suficiente stock disponible.')
            
            self.articulo.save()
        
        super().save(*args, **kwargs)
        if self.venta:
            self.venta.actualizar_total()

    def delete(self, *args, **kwargs):
        # Restaurar el stock al eliminar el detalle
        if self.articulo:
            self.articulo.stock += self.cantidad
            self.articulo.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Detalle venta {self.id} - {self.articulo.nombre if self.articulo else 'N/A'}"