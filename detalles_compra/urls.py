from django.urls import path
from . import views

urlpatterns = [
    path('detalles_compra/', views.lista_detalles_compra, name='lista_detalles_compra'),
    path('detalles_compra/<int:detalle_id>/', views.detalle_detalle_compra, name='detalle_detalle_compra'),
    path('detalles_compra/nuevo/', views.crear_detalle_compra, name='crear_detalle_compra'),
]
