from django.urls import path
from . import views

urlpatterns = [
    path('libreria/lista_detalles_venta/<int:venta_id>/', views.lista_detalles_venta, name='lista_detalles_venta'),
    path('detalles/crear/<int:venta_id>/', views.crear_detalle_venta, name='crear_detalle_venta'),
    path('editar/<int:pk>/', views.editar_detalle_venta, name='editar_detalle_venta'),
    path('eliminar/<int:pk>/', views.eliminar_detalle_venta, name='eliminar_detalle_venta'),
    path('detalles_venta/exportar_pdf/', views.exportar_pdf, name='exportar_pdf'),
    path('detalles_venta/exportar_excel/', views.exportar_excel, name='exportar_excel'),
]
