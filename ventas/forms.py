from django import forms
from .models import Venta
from .models import Article
from django.utils import timezone

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['fecha', 'cliente']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
        }

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
    articulo = forms.ModelChoiceField(
        queryset=Article.objects.all(),
        required=False,
        empty_label="Todos los artículos",
        widget=forms.Select(attrs={'class': 'form-control'})
    )