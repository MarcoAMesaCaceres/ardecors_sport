from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/<int:usuario_id>/', views.detalle_usuario, name='detalle_usuario'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario')
]
