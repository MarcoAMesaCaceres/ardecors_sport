from django import forms
from .models import DetalleVenta

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['articulo', 'cantidad', 'precio_unitario', 'total']
        