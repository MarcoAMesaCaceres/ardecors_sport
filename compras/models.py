from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from proveedores.models import Proveedor

class Compras(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def clean(self):
        if self.fecha and self.fecha > timezone.now().date():
            raise ValidationError({'fecha': "La fecha de compra no puede ser futura."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def actualizar_total(self):
        self.total = sum(detalle.total for detalle in self.detalles.all())
        self.save()

    def __str__(self):
        return f"Orden de compra {self.id} - {self.fecha}"