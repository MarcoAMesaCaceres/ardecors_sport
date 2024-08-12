from django.db import models
from proveedores.models import Proveedor

class Compras(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    producto = models.CharField(max_length=255, default="Producto no especificado")

    def __str__(self):
        return f"Orden {self.id}"