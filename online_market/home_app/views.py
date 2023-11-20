from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib import messages

def article_list(request):
    articles = Article.objects.all()
    form = ArticleForm()

    if request.method == 'POST':
        # Traitement pour ajouter un nouvel article
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')

    return render(request, 'article_list.html', {'articles': articles, 'form': form})

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # Récupérez les données du formulaire
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            color = form.cleaned_data['color']

            # Définissez des valeurs par défaut si les champs sont vides
            if not name:
                name = "Nom par défaut"

            if not price:
                price = 0

            if not color:
                color = "Couleur par défaut"

            try:
                # Créez un nouvel article en utilisant les données du formulaire
                new_article = form.save(commit=False)
                new_article.name = name
                new_article.price = price
                new_article.color = color
                new_article.save()
                messages.success(request, 'L\'article a été ajouté avec succès.')
                return redirect('article_list')
            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite lors de l\'ajout de l\'article : {e}')
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
    
    else:
        form = ArticleForm()

    return render(request, 'add_article.html', {'form': form})

def delete_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.delete()
    return redirect('article_list')

def delete_all_articles(request):
    if request.method == 'POST':
        Article.objects.all().delete()
        return redirect('article_list')
    return render(request, 'article_list.html')