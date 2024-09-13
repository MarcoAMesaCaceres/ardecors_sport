from django.urls import path
from . import views

urlpatterns = [
    path('venta/<int:venta_id>/detalles/', views.lista_detalles_venta, name='lista_detalles_venta'),
    path('venta/<int:venta_id>/detalle/crear/', views.crear_detalle_venta, name='crear_detalle_venta'),
    path('detalle/<int:detalle_id>/editar/', views.editar_detalle_venta, name='editar_detalle_venta'),
    path('detalle/<int:detalle_id>/eliminar/', views.eliminar_detalle_venta, name='eliminar_detalle_venta'),
]
