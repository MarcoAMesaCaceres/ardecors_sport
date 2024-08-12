from django.db import models
from articles.models import Article
from django.utils import timezone

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(default=timezone.now)
    cliente = models.CharField(max_length=100, default='Cliente no especificado')
    producto = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.total = self.cantidad * self.precio_unitario
        super(Venta, self).save(*args, **kwargs)

    def __str__(self):
        return f"Venta {self.id} - {self.cliente} - {self.fecha}"