from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.ardecors, name='ardecors'),
    path('productos/', views.productos, name='productos'),
    path('sobre/', views.sobre, name='sobre'),
    path('contacto/', views.contacto, name='contacto'),
   
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    path('base_articles/', views.base_articles, name='base_articles'),
    path('eliminar_articles/', views.eliminar_articles, name='eliminar_articles'),
    path('editar_articles/', views.editar_articles, name='editar_articles'),
    path('crear_articles/', views.crear_articles, name='crear_articles'),
    path('lista_articles/', views.lista_articles, name='_articles'),
    
    path('base_tareas/', views.base_tareas, name='base_tareas'),
    path('crear_tareas/', views.crear_tareas, name='crear_tareas'),
    path('lista_tareas/', views.lista_tareas, name='lista_tareas'),
    path('editar_tareas/', views.editar_tareas, name='editar_tareas'),
    path('eliminar_tareas/', views.eliminar_tareas, name='eliminar_tareas'),
    
    path('base_compras/', views.base_compras, name='base_compras'),
    path('crear_compras/', views.crear_compras, name='crear_compras'),
    path('lista_compras/', views.lista_compras, name='lista_compras'),
    path('editar_compras/', views.editar_compras, name='editar_compras'),
    path('eliminar_compras/', views.eliminar_compras, name='eliminar_compras'),
    
    path('base_detalle_compra/', views.base_detalle_compra, name='base_detalle_compra'),
    path('crear_detalle_compra/', views.crear_detalle_compra, name='crear_detalle_compra'),
    path('lista_detalles_compra/', views.lista_detalles_compra, name='lista_detalles_compra'),
    path('editar_detalle_compra/', views.editar_detalle_compra, name='editar_detalle_compra'),
    path('eliminar_detalle_compra/', views.eliminar_detalle_compra, name='eliminar_detalle_compra'),
    

    
    path('base_venta/', views.base_venta, name='base_venta'),
    path('crear_venta/', views.crear_venta, name='crear_venta'),
    path('lista_ventas/', views.lista_ventas, name='lista_ventas'),
    path('editar_venta/', views.editar_venta, name='editar_venta'),
    path('eliminar_venta/', views.eliminar_venta, name='eliminar_venta'),
    
    path('base_detalle_venta/', views.base_detalle_venta, name='base_detalle_venta'),
    path('crear_detalle_venta/', views.crear_detalle_venta, name='crear_detalle_venta'),
    path('lista_detalles_venta/', views.lista_detalles_venta, name='lista_detalles_venta'),
    path('editar_detalle_venta/', views.editar_detalle_venta, name='editar_detalle_venta'),
    path('eliminar_detalle_venta/', views.eliminar_detalle_venta, name='eliminar_detalle_venta'),
    
    path('base_proveedor/', views.base_proveedor, name='base_proveedor'),
    path('crear_proveedor/', views.crear_proveedor, name='crear_proveedor'),
    path('lista_proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('editar_proveedor/', views.editar_proveedor, name='editar_proveedora'),
    path('eliminar_proveedor/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('lista_ayuda/', views.lista_ayuda, name='lista_ayuda'),
    path('detalle_ayuda/', views.detalle_ayuda, name='detalle_ayuda'),
    path('base_ayuda/', views.base_ayuda, name='besa_ayuda'),
    
    path('ardecors/', views.ardecors, name='ardecors'),

    path('logout/', views.logout_view, name='logout'),

    
    path('backup_databases/', views.backup_databases, name='backup_databases'),
    
    # Vista para crear un respaldo de la base de datos
    path('backup/create/', views.backup_database, name='backup_database'),
    
    # Vista para listar todos los respaldos disponibles
    path('backup/list/', views.backup_list, name='backup_list'),
    
    # Vista para restaurar la base de datos desde un respaldo específico
    path('backup/restore/', views.restore_database, name='restore_database'),
    
    # Vista para descargar un archivo de respaldo
    path('backup/download/<str:filename>/', views.download_backup, name='download_backup'),
    
    # Vista para eliminar un archivo de respaldo
    path('backup/delete/<str:filename>/', views.delete_backup, name='delete_backup'),
]


