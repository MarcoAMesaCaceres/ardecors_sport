from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['nombre', 'descripcion', 'precio', 'stock']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }
class ArticleSearchForm(forms.Form):
    search_query = forms.CharField(required=False, label='Buscar', widget=forms.TextInput(attrs={'class': 'form-control'}))
    min_price = forms.DecimalField(required=False, label='Precio mínimo', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max_price = forms.DecimalField(required=False, label='Precio máximo', widget=forms.NumberInput(attrs={'class': 'form-control'}))