# forms.py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'price', 'color']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Vous pouvez également définir des valeurs par défaut ici si nécessaire

        # Ajoutez des placeholders pour chaque champ
        self.fields['name'].widget.attrs['placeholder'] = 'Entrez le nom'
        self.fields['price'].widget.attrs['placeholder'] = 'Entrez le prix'
        self.fields['color'].widget.attrs['placeholder'] = 'Entrez la couleur'
