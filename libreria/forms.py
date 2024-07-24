from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario, Producto, Material, TipoDePago, Compra, Venta

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)   

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'primer_nombre', 'segundo_nombre', 'primer_apellido', 
            'segundo_apellido', 'tipo_documento', 'documento', 
            'correo', 'direccion', 'telefono']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['precio', 'tamaño', 'color', 'titulo', 'imagen', 'descripcion', 'nombre']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['tipo', 'calidad', 'precio', 'color', 'tamaño', 'nombre']

class TipoDePagoForm(forms.ModelForm):
    class Meta:
        model = TipoDePago
        fields = ['transferencia', 'efectivo', 'tarjeta']

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['cantidad', 'valor', 'tipo_de_pago']  

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['valor', 'tipo_de_pago']
        