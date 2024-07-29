from django.urls import path
from . import views

urlpatterns = [
    path('ordenes_compras/', views.lista_ordenes_compra, name='lista_ordenes_compras'),
    path('ordenes_compras/<int:orden_id>/', views.detalle_orden_compra, name='detalle_orden_compras'),
    path('ordenes_compras/nuevo/', views.crear_orden_compra, name='crear_orden_compras'),
]
