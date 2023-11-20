from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

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

def delete_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.delete()
    return redirect('article_list')

def delete_all_articles(request):
    if request.method == 'POST':
        Article.objects.all().delete()
        return redirect('article_list')
    return render(request, 'article_list.html')