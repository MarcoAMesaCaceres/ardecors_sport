from django import forms
from .models import OrdenCompra

class OrdenCompraForm(forms.ModelForm):
    class Meta:
        model = OrdenCompra
        fields = ['fecha', 'proveedor', 'total']