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
    
    # URLs para ventas
    
    path('ventas/crear_venta/', views.crear_venta, name='crear_venta'),
    

    # URLs para usuarios
    
    path('usuarios/crear_usuario/', views.crear_usuario, name='crear_usuario'),
   

    # URLs para órdenes de compra
    
    path('ordenes_compras/crear_orden_compra/', views.crear_orden_compra, name='crear_orden_compra'),
    

    # URLs para proveedores
    
    path('proveedores/crear_proveedor/', views.crear_proveedor, name='crear_proveedor'),
    

    # URLs para detalles de compra
    
    path('detalles_compra/crear/', views.crear_detalle_compra, name='crear_detalle_compra'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('pagar/', views.pagar, name='pagar'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('logout/', views.logout_view, name='logout'),
]
