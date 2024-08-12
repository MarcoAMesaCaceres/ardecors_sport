from import_export import resources
from import_export.admin import ExportMixin
from django.contrib import admin
from .models import Venta

class VentaResource(resources.ModelResource):
    class Meta:
        model = Venta
        fields = ('id', 'fecha', 'cliente', 'producto__nombre', 'cantidad', 'precio_unitario', 'total')

class VentaAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = VentaResource
    list_display = ('id', 'fecha', 'cliente', 'producto', 'cantidad', 'precio_unitario', 'total')

admin.site.register(Venta, VentaAdmin)
