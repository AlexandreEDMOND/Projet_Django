# forms.py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'price', 'color']
        widgets = {
            'name': forms.TextInput(attrs={'value': 'Nom par défaut'}),
            'price': forms.NumberInput(attrs={'value': 0.0}),
            'color': forms.TextInput(attrs={'value': 'Couleur par défaut'}),
        }
