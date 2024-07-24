from django.urls import path
from . import views

urlpatterns = [
    path('', views.ardecors, name='ardecors'),
    path('productos/', views.productos, name='productos'),
    path('sobre/', views.sobre, name='sobre'),
    path('contacto/', views.contacto, name='contacto'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/', views.registro, name='registro'),
]

