from django import forms
from .models import Venta
from .models import Article
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
    cliente = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del cliente'})
    )
    fecha_inicio = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    fecha_fin = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    total_min = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total mínimo', 'step': '0.01'})
    )
    total_max = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total máximo', 'step': '0.01'})
    )
    articulo = forms.ModelChoiceField(
        queryset=Article.objects.all(),
        required=False,
        empty_label="Todos los artículos",
        widget=forms.Select(attrs={'class': 'form-control'})
    )