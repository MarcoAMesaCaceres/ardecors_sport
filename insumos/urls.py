from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_insumos, name='lista_insumos'),
    path('crear/', views.crear_insumos, name='crear_insumos'),
    path('editar/<int:pk>/', views.editar_insumos, name='editar_insumos'),
    path('eliminar/<int:pk>/', views.eliminar_insumos, name='eliminar_insumos')]