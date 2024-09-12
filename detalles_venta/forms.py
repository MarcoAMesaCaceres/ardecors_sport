from django import forms
from .models import Article
from .models import DetalleVenta
from decimal import Decimal
from django import forms
from .models import Article, DetalleVenta
from decimal import Decimal
class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['articulo', 'cantidad', 'precio_unitario']
        widgets = {
            'articulo': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.01'}),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad <= 0:
            raise forms.ValidationError("La cantidad debe ser un número positivo.")
        return cantidad

    def clean_precio_unitario(self):
        precio_unitario = self.cleaned_data.get('precio_unitario')
        if precio_unitario <= Decimal('0'):
            raise forms.ValidationError("El precio unitario debe ser un número positivo.")
        return precio_unitario

    def clean(self):
        cleaned_data = super().clean()
        articulo = cleaned_data.get('articulo')
        cantidad = cleaned_data.get('cantidad')
        if articulo and cantidad:
            if articulo.stock < cantidad:
                raise forms.ValidationError(f"No hay suficiente stock para este artículo. Stock disponible: {articulo.stock}")
        return cleaned_data
class DetalleVentaSearchForm(forms.Form):
    articulo = forms.ModelChoiceField(
        queryset=Article.objects.all(),
        required=False,
        empty_label="Todos los artículos",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    cantidad_min = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad mínima'})
    )
    cantidad_max = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad máxima'})
    )
    precio_unitario_min = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio mínimo', 'step': '0.01'})
    )
    precio_unitario_max = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio máximo', 'step': '0.01'})
    )

   