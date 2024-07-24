from django.db import models
from django.contrib import admin

# Create your models here.
class TipoDePago(models.Model):
    id_de_pago = models.AutoField(primary_key=True)
    efectivo = models.BooleanField(default=False)
    tarjeta = models.BooleanField(default=False)
    transferencia = models.BooleanField(default=False)

    def __str__(self):
        return f"Transferencia: {self.transferencia}, Efectivo: {self.efectivo}, Tarjeta: {self.tarjeta}"

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)  # Cambiado a AutoField
    tamaño = models.IntegerField(null=True, blank=True)
    color = models.TextField(null=True, blank=True)
    titulo = models.CharField(max_length=100, verbose_name='Título', null=True, blank=True)
    imagen = models.ImageField(upload_to='imagenes', verbose_name='Imagen', null=True)
    descripcion = models.TextField(verbose_name='Descripción', null=True, blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Título: {self.titulo} - Descripción: {self.descripcion}"

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class TipoDeProducto(models.Model):
    id_tipo_de_producto = models.AutoField(primary_key=True)  # Cambiado a AutoField
    nombre = models.TextField(null=True)
    referencia = models.TextField(null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)



class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)  # Cambiado a AutoField
    cantidad = models.IntegerField(null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Cambiado a DecimalField
    fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    tipo_de_pago = models.ForeignKey(TipoDePago, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"Compra valor: {self.valor}, Cantidad: {self.cantidad}"

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tipo_de_pago = models.ForeignKey(TipoDePago, on_delete=models.CASCADE, null=True, blank=True)

class Material(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    calidad = models.CharField(max_length=50)
    tamaño = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre