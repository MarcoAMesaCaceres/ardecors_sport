from django import forms
from insumos.models import Insumos
from django.core.exceptions import ValidationError

class InsumosForm(forms.ModelForm):
    class Meta:
        model = Insumos
        fields = ['nombre', 'descripcion','proveedor', 'precio', 'stock']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del insumo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del insumo'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.01', 'placeholder': 'Precio'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Cantidad en stock'}),
            
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not all(char.isalnum() or char.isspace() or char in 'áéíóúÁÉÍÓÚñÑ' for char in nombre):
            raise ValidationError("El nombre solo puede contener letras (incluyendo tildes), números y espacios.")
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if descripcion and len(descripcion) < 5:
            raise ValidationError("La descripción debe tener al menos 5 caracteres.")
        return descripcion

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio and precio <= 0:
            raise ValidationError("El precio debe ser un número positivo.")
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock and stock < 0:
            raise ValidationError("El stock debe ser un número positivo o cero.")
        return stock
