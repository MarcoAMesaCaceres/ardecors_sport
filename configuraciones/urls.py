from django.urls import path
from configuraciones import views

urlpatterns = [
    path('configuraciones/', views.lista_configuraciones, name='lista_configuraciones'),
    path('crear/', views.crear_configuracion, name='crear_configuracion'),
    path('editar/<int:pk>/', views.editar_configuracion, name='editar_configuracion'),
    path('<int:pk>/eliminar/', views.eliminar_configuraciones, name='eliminar_configuraciones'),
]
