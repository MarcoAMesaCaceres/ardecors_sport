from django import forms
from .models import Article
from django.core.exceptions import ValidationError

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['nombre', 'descripcion', 'precio', 'stock']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.replace(' ', '').isalpha():
            raise ValidationError("El nombre solo puede contener letras y espacios.")
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if descripcion and len(descripcion) < 10:
            raise ValidationError("La descripción debe tener al menos 10 caracteres.")
        return descripcion

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise ValidationError("El precio debe ser un número positivo.")
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise ValidationError("El stock debe ser un número positivo o cero.")
        return stock

class ArticleSearchForm(forms.Form):
    search_query = forms.CharField(required=False, label='Buscar', widget=forms.TextInput(attrs={'class': 'form-control'}))
    min_price = forms.DecimalField(required=False, label='Precio mínimo', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max_price = forms.DecimalField(required=False, label='Precio máximo', widget=forms.NumberInput(attrs={'class': 'form-control'}))