from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ayuda, name='lista_ayuda'),
    path('<int:pk>/', views.detalle_ayuda, name='detalle_ayuda'),
    path('manual_usuario/', views.manual_usuario, name='manual_usuario'),
    path('descargar-manual/', views.descargar_manual, name='descargar_manual'),
]