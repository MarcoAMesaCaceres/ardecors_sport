from django import forms
from .models import DetalleCompra

class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['articulo', 'cantidad', 'precio_unitario', 'total']