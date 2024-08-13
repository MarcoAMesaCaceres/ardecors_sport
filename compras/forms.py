from django import forms
from .models import Compras

class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compras
        fields = ['fecha', 'proveedor', 'total', 'producto']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'producto': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_total(self):
        total = self.cleaned_data.get('total')
        if total <= 0:
            raise forms.ValidationError("El total debe ser un número positivo.")
        return total

    def clean_producto(self):
        producto = self.cleaned_data.get('producto')
        if not all(char.isalnum() or char.isspace() for char in producto):
            raise forms.ValidationError("El producto solo puede contener letras, números y espacios.")
        return producto

class ComprasSearchForm(forms.Form):
    search_query = forms.CharField(required=False, label='Buscar', widget=forms.TextInput(attrs={'class': 'form-control'}))
    min_total = forms.DecimalField(required=False, label='Total mínimo', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max_total = forms.DecimalField(required=False, label='Total máximo', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    fecha_inicio = forms.DateField(required=False, label='Fecha inicio', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    fecha_fin = forms.DateField(required=False, label='Fecha fin', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))