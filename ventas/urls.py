from django.urls import path
from . import views

urlpatterns = [
    path('ventas/', views.lista_ventas, name='lista_ventas'),
    path('ventas/<int:venta_id>/', views.detalle_venta, name='detalle_venta'),
    path('ventas/nuevo/', views.crear_venta, name='crear_venta'),
    path('<int:pk>/eliminar/', views.eliminar_venta, name='eliminar_venta'),
]
