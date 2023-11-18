from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article
from .forms import ArticleForm

# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    template = loader.get_template('article_list.html')
    context = {
        'articles': articles,
    }
    return HttpResponse(template.render(context, request))

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # Récupérez les données des champs input supplémentaires
            Nom = request.POST.get('Nom', 'default')
            Prix = request.POST.get('Prix', '0')
            Couleur = request.POST.get('Couleur', 'None')

            try:
                # Créez un nouvel article en utilisant les données du formulaire
                new_article = form.save(commit=False)
                new_article.name = Nom 
                new_article.price = Prix
                new_article.color = Couleur
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