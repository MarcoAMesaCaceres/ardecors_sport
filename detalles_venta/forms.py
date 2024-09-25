from django import forms
from .models import DetalleVenta

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['articulo', 'cantidad', 'precio_unitario']
        widgets = {
            'articulo': forms.Select(attrs={'class': 'form-control', 'id': 'id_articulo'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'id': 'id_cantidad'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'step': '0.01', 'readonly': True, 'id': 'id_precio_unitario'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['precio_unitario'].required = False

    def clean(self):
        cleaned_data = super().clean()
        articulo = cleaned_data.get('articulo')
        cantidad = cleaned_data.get('cantidad')
        if articulo and cantidad:
            if articulo.stock < cantidad:
                raise forms.ValidationError(f"No hay stock suficiente. Stock disponible: {articulo.stock}")
        return cleaned_data