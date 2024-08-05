from django.urls import path
from . import views

urlpatterns = [
    path('venta/<int:venta_id>/', views.detalle_venta, name='detalle_venta'),
    path('ventas/', views.lista_ventas, name='lista_ventas'),
    path('crear/', views.crear_venta, name='crear_venta'),
    path('editar/<int:pk>/', views.editar_venta, name='editar_venta'),
    path('<int:pk>/eliminar/', views.eliminar_venta, name='eliminar_venta'),
]
