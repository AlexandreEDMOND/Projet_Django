from django.urls import path
from . import views

urlpatterns = [
    path('article_list/', views.article_list, name='article_list'),
    path('delete_article/<int:article_id>/', views.delete_article, name='delete_article'),
    # Ajoutez d'autres URL au besoin
]