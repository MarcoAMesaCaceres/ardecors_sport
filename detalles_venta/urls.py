from django.urls import path
from . import views

urlpatterns = [
    path('detalles_venta/', views.lista_detalles_venta, name='lista_detalles_venta'),
    path('detalles_venta/<int:detalle_id>/', views.detalle_detalle_venta, name='detalle_detalle_venta'),
    path('detalles_venta/nuevo/', views.crear_detalle_venta, name='crear_detalle_venta'),
]
