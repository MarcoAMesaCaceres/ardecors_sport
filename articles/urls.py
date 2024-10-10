from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_articles, name='lista_articles'),
    path('crear/', views.crear_articles, name='crear_articles'),
    path('editar/<int:pk>/', views.editar_articles, name='editar_articles'),
    path('eliminar/<int:pk>/', views.eliminar_articles, name='eliminar_articles')
    path('verificar-stock/<int:article_id>/', verificar_stock, name='verificar_stock'),
    ]