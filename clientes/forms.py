from django import forms
from .models import Clientes

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['documento', 'nombre', 'telefono', 'email', 'direccion']
        widgets = {
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean_documento(self):
        documento = self.cleaned_data.get('documento')
        if not documento.isdigit() or len(documento) < 8 or len(documento) > 10:
            raise forms.ValidationError('El número de documento debe tener entre 8 y 10 dígitos.')
        return documento

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.replace(' ', '').isalpha():
            raise forms.ValidationError('El nombre solo puede contener letras y espacios.')
        return nombre

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono:
            telefono = telefono.replace(' ', '')  # Eliminar espacios
            if not telefono.startswith('+57'):
                telefono = '+57' + telefono
            if not telefono.startswith('+573') or len(telefono) != 13:
                raise forms.ValidationError('El número de teléfono debe tener el formato +57 seguido de 10 dígitos y ser un número válido de Colombia (+573XXXXXXXXX).')
        return telefono

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        telefono = cleaned_data.get('telefono')

        if not email and not telefono:
            raise forms.ValidationError('Debe proporcionar al menos un email o un número de teléfono.')

        return cleaned_data