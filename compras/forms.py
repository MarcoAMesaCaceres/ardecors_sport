from django import forms
from .models import Compras

class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compras
        fields = ['fecha', 'proveedor', 'total', 'producto']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }