from django.urls import path
from . import views

urlpatterns = [
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/<int:proveedor_id>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('proveedores/nuevo/', views.crear_proveedor, name='crear_proveedor'),
    path('<int:pk>/eliminar/', views.eliminar_proveedor, name='eliminar_proveedor'),
]
