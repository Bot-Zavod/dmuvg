from django.shortcuts import render, redirect
from website.models import Article


def article_feed(request):
    return render(request, "article_feed.html")


def article(request):
    article = Article.objects.get(pk=2)
    context = {'article': article}
    return render(request, "article.html", context)


def article_edit(request):
    article = Article.objects.get(pk=1)
    context = {'article': article}
    return render(request, "article_edit.html", context)