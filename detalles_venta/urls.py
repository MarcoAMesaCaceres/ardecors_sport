from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_detalles_venta, name='lista_detalles_venta'),
    path('crear/', views.crear_detalle_venta, name='crear_detalle_venta'),
    path('editar/<int:pk>/', views.editar_detalle_venta, name='editar_detalle_venta'),
    path('eliminar/<int:pk>/', views.eliminar_detalle_venta, name='eliminar_detalle_venta'),
]
