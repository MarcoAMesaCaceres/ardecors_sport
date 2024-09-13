from django import forms
from .models import Compras

class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compras
        fields = ['fecha', 'proveedor']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
        }