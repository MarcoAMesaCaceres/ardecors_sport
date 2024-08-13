from django import forms
from .models import Venta
from django.core.exceptions import ValidationError
from django.utils import timezone
class VentaForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Venta
        fields = ['fecha', 'cliente', 'producto', 'cantidad', 'precio_unitario']
        widgets = {
            'cliente': forms.TextInput(attrs={'placeholder': 'Nombre del cliente'}),
            'cantidad': forms.NumberInput(attrs={'min': 1}),
            'precio_unitario': forms.NumberInput(attrs={'step': '0.01', 'min': '0.01'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        cantidad = cleaned_data.get('cantidad')
        precio_unitario = cleaned_data.get('precio_unitario')
        fecha = cleaned_data.get('fecha')
        
        if cantidad and cantidad <= 0:
            raise ValidationError('La cantidad debe ser mayor que cero.')
        
        if precio_unitario and precio_unitario <= 0:
            raise ValidationError('El precio unitario debe ser mayor que cero.')
        
        if fecha and fecha > timezone.now().date():
            raise ValidationError('La fecha de venta no puede ser futura.')
        
        if cantidad and precio_unitario:
            cleaned_data['total'] = cantidad * precio_unitario
        
        return cleaned_data

    def save(self, commit=True):
        venta = super().save(commit=False)
        venta.total = venta.cantidad * venta.precio_unitario
        if commit:
            venta.save()
        return venta