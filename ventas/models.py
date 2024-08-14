from django.db import models
from articles.models import Article

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    cliente = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    articulo = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"Venta {self.id}"