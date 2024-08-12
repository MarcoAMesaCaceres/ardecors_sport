from django.db import models
import datetime
class DetalleCompra(models.Model):
    id = models.AutoField(primary_key=True)
    compra = models.ForeignKey('compras.Compras', on_delete=models.CASCADE, related_name='detalles', to_field='id', null=True)
    fecha = models.DateField(default=datetime.date.today)
    producto = models.CharField(max_length=255, default="Producto Desconocido") 
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle de compra {self.id} - {self.producto} - Orden {self.compra.id if self.compra else 'N/A'}"

    def save(self, *args, **kwargs):
        self.total = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)