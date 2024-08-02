from django.urls import path
from configuraciones import views

urlpatterns = [
    path('configuraciones/', views.lista_configuraciones, name='lista_configuraciones'),
    path('configuraciones/<int:config_id>/', views.detalle_configuracion, name='detalle_configuracion'),
    path('configuraciones/nuevo/', views.crear_configuracion, name='crear_configuracion'),
    path('<int:pk>/eliminar/', views.eliminar_configuracion, name='eliminar_configuracion'),
]
