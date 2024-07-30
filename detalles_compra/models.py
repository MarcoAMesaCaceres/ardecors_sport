from django.db import models
from django.apps import apps

class DetalleOrdenCompra(models.Model):
    orden = models.ForeignKey('ordenes_compras.OrdenCompra', on_delete=models.CASCADE)
    producto = models.ForeignKey('articles.Article', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.producto