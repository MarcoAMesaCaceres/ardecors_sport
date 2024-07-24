from django.urls import path
from . import views

urlpatterns = [
    path('ordenes_compra/', views.lista_ordenes_compra, name='lista_ordenes_compra'),
    path('ordenes_compra/<int:orden_id>/', views.detalle_orden_compra, name='detalle_orden_compra'),
    path('ordenes_compra/nuevo/', views.crear_orden_compra, name='crear_orden_compra'),
]
