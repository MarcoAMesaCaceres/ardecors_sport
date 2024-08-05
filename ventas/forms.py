from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Venta
<<<<<<< HEAD
        fields = ['fecha', 'total']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
=======
        fields = ['fecha', 'cliente', 'producto', 'cantidad', 'precio_unitario']
        widgets = {
            'cliente': forms.TextInput(attrs={'placeholder': 'Nombre del cliente'}),
            'cantidad': forms.NumberInput(attrs={'min': 1}),
            'precio_unitario': forms.NumberInput(attrs={'step': '0.01'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        cantidad = cleaned_data.get('cantidad')
        precio_unitario = cleaned_data.get('precio_unitario')
        
        if cantidad and precio_unitario:
            cleaned_data['total'] = cantidad * precio_unitario
        
        return cleaned_data

    def save(self, commit=True):
        venta = super().save(commit=False)
        venta.total = venta.cantidad * venta.precio_unitario
        if commit:
            venta.save()
        return venta
>>>>>>> 0a34752b090361f8739dbee642db00051a5ec43b
