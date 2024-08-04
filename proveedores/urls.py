from django.urls import path
from . import views

urlpatterns = [
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/nuevo/', views.crear_proveedor, name='crear_proveedor'),
    path('<int:pk>/eliminar/', views.eliminar_proveedor, name='eliminar_proveedor'),
]
