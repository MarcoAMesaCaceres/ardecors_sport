from django.db import models
from articles.models import Article

class DetalleVenta(models.Model):
    articulo = models.ForeignKey(Article, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.articulo.nombre} - {self.cantidad}"
