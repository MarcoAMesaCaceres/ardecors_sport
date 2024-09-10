from django import forms
from .models import DetalleCompra

class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['compra', 'fecha', 'cantidad', 'precio_unitario']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs and kwargs['instance']:
            self.fields['producto'] = forms.CharField(
                initial=kwargs['instance'].producto,
                disabled=True,
                required=False
            )
        elif 'initial' in kwargs and 'compra' in kwargs['initial']:
            self.fields['producto'] = forms.CharField(
                initial=kwargs['initial']['compra'].producto,
                disabled=True,
                required=False
            )

    def clean(self):
        cleaned_data = super().clean()
        cantidad = cleaned_data.get('cantidad')
        precio_unitario = cleaned_data.get('precio_unitario')
        
        if cantidad and precio_unitario:
            cleaned_data['total'] = cantidad * precio_unitario
        
        return cleaned_data