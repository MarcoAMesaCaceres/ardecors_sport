from django import forms
from .models import Article
from django.core.exceptions import ValidationError

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del artículo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del artículo'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.01', 'placeholder': 'Precio'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Cantidad en stock'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.replace(' ', '').isalnum():
            raise ValidationError("El nombre solo puede contener letras, números y espacios.")
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if descripcion and len(descripcion) < 10:
            raise ValidationError("La descripción debe tener al menos 10 caracteres.")
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

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if imagen:
            if imagen.size > 5 * 1024 * 1024:  # 5MB limit
                raise ValidationError("El tamaño de la imagen no debe exceder 5MB.")
            ext = imagen.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png', 'gif']:
                raise ValidationError("Solo se permiten archivos de imagen (jpg, jpeg, png, gif).")
        return imagen