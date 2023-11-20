from django.urls import path
from . import views

urlpatterns = [
    path('article_list/', views.article_list, name='article_list'),
    path('add_article/', views.add_article, name='add_article'),
    path('delete_article/<int:article_id>/', views.delete_article, name='delete_article'),
    path('delete_all_articles/', views.delete_all_articles, name='delete_all_articles'),
]