from django.db import models
from ventas.models import Venta
from articles.models import Article
# Create your models here.

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Article, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    # Otros campos relevantes para Producto

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    # Campos relevantes para Venta

    def __str__(self):
        return str(self.id)

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"