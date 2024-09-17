from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('crear/', views.crear_clientes, name='crear_clientes'),
    path('editar/<int:pk>/', views.editar_clientes, name='editar_clientes'),
    path('eliminar/<int:pk>/', views.eliminar_clientes, name='eliminar_clientes'),
]
