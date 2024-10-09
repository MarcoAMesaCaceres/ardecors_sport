from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
import zoneinfo
from proveedores.models import Proveedor

class Compras(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=timezone.localtime) 
    proveedor = models.ForeignKey(
        Proveedor, 
        on_delete=models.PROTECT,  # Cambiado a PROTECT para evitar eliminación accidental
        related_name='compras'
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = "Compras"

    def actualizar_total(self):
        self.total = sum(detalle.total for detalle in self.detalles.all())
        self.save()

    def __str__(self):
        return f"Compra {self.id} - {self.proveedor.nombre} - {timezone.localtime(self.fecha).strftime('%d/%m/%Y %I:%M %p')}"
