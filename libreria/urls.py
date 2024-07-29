from django.urls import path
from . import views

urlpatterns = [
path('', views.ardecors, name='ardecors'),
    path('productos/', views.productos, name='productos'),
    path('sobre/', views.sobre, name='sobre'),
    path('contacto/', views.contacto, name='contacto'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/', views.registro, name='registro'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('configuraciones/', views.configuraciones, name='configuraciones'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('ordenes_compras/', views.ordenes_compras, name='ordenes_compras'),
    path('detalles_compra/', views.detalles_compra, name='detalles_compra'),
    path('detalles_venta/', views.detalles_venta, name='detalles_venta'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('ventas/', views.ventas, name='ventas'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('pagar/', views.pagar, name='pagar'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('logout/', views.logout_view, name='logout'),
]
