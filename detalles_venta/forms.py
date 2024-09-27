from django import forms
from .models import DetalleVenta

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['articulo', 'cantidad']
        widgets = {
            'articulo': forms.Select(attrs={'class': 'form-control', 'id': 'id_articulo'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'id': 'id_cantidad'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        articulo = cleaned_data.get('articulo')
        cantidad = cleaned_data.get('cantidad')
        if articulo and cantidad:
            if articulo.stock < cantidad:
                raise forms.ValidationError(f"No hay stock suficiente. Stock disponible: {articulo.stock}")
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.precio_unitario = instance.articulo.precio
        if commit:
            instance.save()
        return instance