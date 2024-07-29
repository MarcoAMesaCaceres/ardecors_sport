from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.lista_articles, name='lista_articles'),
    path('articles/<int:producto_id>/', views.detalle_articles, name='detalle_articles'),
    path('articles/crear/', views.crear_articles, name='crear_articles'),
]