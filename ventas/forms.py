from django import forms
from .models import Venta
from clientes.models import Clientes
from django.utils import timezone

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['fecha', 'clientes']  # Cambiado de 'cliente' a 'clientes'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'clientes': forms.Select(attrs={'class': 'form-control'}),  # Cambiado de 'cliente' a 'clientes'
        }

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha > timezone.now().date():
            raise forms.ValidationError("La fecha de venta no puede ser futura.")
        return fecha
