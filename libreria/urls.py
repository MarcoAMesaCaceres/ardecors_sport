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
    path('eliminar_articles/', views.eliminar_articles, name='eliminar_articles'),
    path('editar_articles/', views.editar_articles, name='editar_articles'),
    path('crear_articles/', views.crear_articles, name='crear_articles'),
    path('lista_articles/', views.lista_articles, name='_articles'),
    path('base_articles/', views.base_articles, name='base_articles'),
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
    path('ardecors/', views.ardecors, name='ardecors'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('logout/', views.logout_view, name='logout'),
]
