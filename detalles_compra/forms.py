from django import forms
from .models import DetalleOrdenCompra

class DetalleOrdenCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleOrdenCompra
        fields = ['orden', 'producto', 'cantidad', 'precio']