from django import forms
from .models import Venta
from django.utils import timezone

class VentaForm(forms.ModelForm):
    fecha = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'step': '60',  # Para mostrar solo minutos, no segundos
                'readonly': True  # Hace que el campo sea solo lectura
            }
        ),
        initial=lambda: timezone.localtime(timezone.now())
    )

    class Meta:
        model = Venta
        fields = ['fecha', 'cliente']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.initial.get('fecha'):
            bogota_now = timezone.localtime(timezone.now())
            self.initial['fecha'] = bogota_now.strftime('%Y-%m-%dT%H:%M')
