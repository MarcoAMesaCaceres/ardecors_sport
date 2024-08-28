from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from usuarios.views import CustomLoginView, CustomPasswordResetView
from .views import register
from . import views
urlpatterns = [
    
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/edit/', views.user_edit, name='user_edit'),
    path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),
]