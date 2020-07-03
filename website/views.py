from django.shortcuts import render, redirect, render_to_response
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from website.models import Article
from .forms import ArticleForm


def detail_article_view(request, slug):
    article = Article.objects.get(slug=slug)
    queryset = Article.objects.filter(fixed_to_top=False)
    if request.method == 'POST' and request.user.is_authenticated:
        if not article.fixed_to_top:
            article.delete()
            return redirect("/")

    context = {
        'object': article,
        'articles': queryset,
    }
    return render(request, 'website/article_detail.html', context)


def article_list_view(request, slug, categ=None):
    FEED_SECTIONS = {
        "vodogospodarska-obstanovka": "WS",
        "ekologo-prosvitnitski-zakhodi": "EV",
        "planirovanie-upravlenii-baseinami": "MR",
    }
    slug = FEED_SECTIONS[slug]
    queryset = Article.objects.filter(category=slug)

    titile = {
        'WS': 'Водогосподарська обстановка',
        'EV': 'Еколого-просвітницькі заходи',
        'MR': 'Управління річковими басейнами'
    }
    context = {
        "object_list": queryset,
        "title": titile[slug],
    }
    return render(request, "website/article_list.html", context)


class Article_Main_List_View(ListView):
    queryset = Article.objects.filter(fixed_to_top=False)


def create_article_view(request):

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            a = Article.objects.create(**form_data)
            return redirect(a.get_absolute_url())
    else:
        form = ArticleForm()
    return render(request, 'article_edit.html', {'form': form})


def edit_article_view(request, slug):
    article = Article.objects.get(slug=slug)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect(article.get_absolute_url())
    context = {
        'form': form,
        'edit': True,
        'category': article.get_category(),
    }
    return render(request, 'article_edit.html', context=context)


def not_found(request):
    return render(request, "page_not_found.html")
