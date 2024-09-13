from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_compras, name='lista_compras'),
    path('crear/', views.crear_compras, name='crear_compras'),
    path('editar/<int:pk>/', views.editar_compras, name='editar_compras'),
    path('eliminar/<int:pk>/', views.eliminar_compras, name='eliminar_compras'),
    path('compras/exportar_excel/',views.exportar_excel, name='exportar_excel'),
    
]