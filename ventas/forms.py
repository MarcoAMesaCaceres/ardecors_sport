from django import forms
from .models import Venta
from django.utils import timezone

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['fecha', 'cliente', 'total', 'articulo']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'articulo': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_total(self):
        total = self.cleaned_data.get('total')
        if total is not None and total <= 0:
            raise forms.ValidationError("El total debe ser un número positivo.")
        return total


    def clean_cliente(self):
        cliente = self.cleaned_data.get('cliente')
        if not cliente:
            raise forms.ValidationError("El nombre del cliente es requerido.")
        if not all(char.isalnum() or char.isspace() for char in cliente):
            raise forms.ValidationError("El nombre del cliente solo puede contener letras, números y espacios.")
        return cliente

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha > timezone.now().date():
            raise forms.ValidationError("La fecha de venta no puede ser futura.")
        return fecha

    def clean(self):
        cleaned_data = super().clean()
        articulo = cleaned_data.get('articulo')
        if articulo and articulo.stock < 1:
            raise forms.ValidationError("No hay stock suficiente para este artículo.")
        return cleaned_data


class VentaSearchForm(forms.Form):
    cliente = forms.CharField(required=False, label='Cliente')
    fecha_inicio = forms.DateField(required=False, label='Fecha inicio', widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_fin = forms.DateField(required=False, label='Fecha fin', widget=forms.DateInput(attrs={'type': 'date'}))
    total_min = forms.DecimalField(required=False, label='Total mínimo')
    total_max = forms.DecimalField(required=False, label='Total máximo')
    
    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        total_min = cleaned_data.get('total_min')
        total_max = cleaned_data.get('total_max')

        if fecha_inicio and fecha_fin and fecha_inicio > fecha_fin:
            raise forms.ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")

        if total_min and total_max and total_min > total_max:
            raise forms.ValidationError("El total mínimo no puede ser mayor que el total máximo.")
