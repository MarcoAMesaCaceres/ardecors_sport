from django.urls import path
from . import views

urlpatterns = [
    path('tareas/', views.lista_tareas, name='lista_tareas'),
    path('crear/', views.crear_tareas, name='crear_tareas'),
    path('editar/<int:pk>/', views.editar_tareas, name='editar_tareas'),
    path('<int:pk>/eliminar/', views.eliminar_tareas, name='eliminar_tareas'),
]
