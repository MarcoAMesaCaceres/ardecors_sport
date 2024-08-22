from django.urls import path
from . import views

urlpatterns = [
    path('ventas/', views.lista_ventas, name='lista_ventas'),
    path('crear/', views.crear_venta, name='crear_venta'),
    path('editar/<int:pk>/', views.editar_venta, name='editar_venta'),
    path('eliminar/<int:pk>/', views.eliminar_venta, name='eliminar_venta'),
    path('ventas/exportar_pdf/', views.exportar_pdf, name='exportar_pdf'),
    path('ventas/exportar_excel/', views.exportar_excel, name='exportar_excel'),
    path('exportar-pdf/', views.exportar_pdf, name='exportar_pdf'),
    path('exportar-excel/', views.exportar_excel, name='exportar_excel'),
]
