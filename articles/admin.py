from django.contrib import admin
from .models import Article  # Cambia de articles a Article

# Registra tus modelos aquí
admin.site.register(Article)