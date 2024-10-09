from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
import zoneinfo

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=timezone.localtime)
    cliente = models.ForeignKey(
        'clientes.Clientes',
        on_delete=models.PROTECT,
        related_name='ventas',
        null=True,
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    

    def actualizar_total(self):
        self.total = sum(detalle.total for detalle in self.detalles.all())
        self.save()
    def __str__(self):
        return f"Venta {self.id} - {self.cliente.nombre if self.cliente else 'Sin cliente'} - {timezone.localtime(self.fecha).strftime('%d/%m/%Y %I:%M %p')}"