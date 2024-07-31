from django.db import models
from proveedores.models import Proveedor

class OrdenCompra(models.Model):
    fecha = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Orden {self.id}"
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    # Otros campos relevantes para Proveedor

    def __str__(self):
        return self.nombre

class OrdenCompra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Orden {self.id} - {self.proveedor.nombre}"