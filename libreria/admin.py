from django.contrib import admin
from .models import Producto
# Register your models here.
admin.site.register(Producto)
from .models import TipoDePago, TipoDeProducto, Producto, Usuario, Compra, Venta, Material

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'tamaño', 'color')
    search_fields = ('nombre', 'descripcion')

@admin.register(TipoDeProducto)
class TipoDeProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'referencia', 'producto')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('primer_nombre', 'primer_apellido', 'correo')
    search_fields = ('primer_nombre', 'documento')

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id_compra', 'cantidad', 'valor', 'fecha', 'tipo_de_pago')
    search_fields = ('id_compra',)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id_venta', 'fecha', 'valor', 'tipo_de_pago')
    search_fields = ('id_venta',)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'calidad', 'tamaño', 'color', 'tipo')
    search_fields = ('nombre',)