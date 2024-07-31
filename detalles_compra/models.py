from django.db import models
from django.apps import apps

class DetalleOrdenCompra(models.Model):
    orden = models.ForeignKey('ordenes_compras.OrdenCompra', on_delete=models.CASCADE)
    producto = models.ForeignKey('articles.Article', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.producto
    

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    # Otros campos relevantes para Producto

    def __str__(self):
        return self.nombre

class Orden(models.Model):
    # Campos relevantes para Orden

    def __str__(self):
        return str(self.id)

class DetalleCompra(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"    