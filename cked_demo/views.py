
from django.views.generic import ListView, DetailView
from .models import Article


class ArticleList(ListView):
    model = Article
    template_name = "main.html"
    context_object_name = "articles_list"


class ArticleDetail(DetailView):
    model = Article
    template_name = "article.html"
    context_object_name = "article"
    pk_url_kwarg = 'id'

