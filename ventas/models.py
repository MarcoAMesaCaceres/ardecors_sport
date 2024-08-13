from django.db import models
from articles.models import Article
from django.utils import timezone
from django.core.exceptions import ValidationError

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(default=timezone.now)
    cliente = models.CharField(max_length=100, default='Cliente no especificado')
    producto = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def clean(self):
        if self.cantidad <= 0:
            raise ValidationError('La cantidad debe ser mayor que cero.')
        if self.precio_unitario <= 0:
            raise ValidationError('El precio unitario debe ser mayor que cero.')
        if self.fecha > timezone.now().date():
            raise ValidationError('La fecha de venta no puede ser futura.')

    def save(self, *args, **kwargs):
        self.full_clean()
        self.total = self.cantidad * self.precio_unitario
        super(Venta, self).save(*args, **kwargs)

    def __str__(self):
        return f"Venta {self.id} - {self.cliente} - {self.fecha}"