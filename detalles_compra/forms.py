from django import forms
from .models import DetalleCompra
from insumos.models import Insumos

class DetalleCompraForm(forms.ModelForm):
    insumo = forms.ModelChoiceField(
        queryset=Insumos.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control w-100'}),
        label='Insumo'
    )

    class Meta:
        model = DetalleCompra
        fields = ['insumo', 'cantidad']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'class': 'form-control w-100'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.insumo:
            self.fields['insumo'].initial = self.instance.insumo

    def clean(self):
        cleaned_data = super().clean()
        insumo = cleaned_data.get('insumo')
        cantidad = cleaned_data.get('cantidad')
        
        if insumo and cantidad:
            if cantidad > insumo.stock:
                raise forms.ValidationError(f"La cantidad no puede ser mayor que el stock disponible ({insumo.stock}).")
            cleaned_data['precio_unitario'] = insumo.precio
            cleaned_data['total'] = cantidad * insumo.precio
        
        return cleaned_data