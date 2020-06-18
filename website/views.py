from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")


def article_edit(request):
    return render(request, "article_edit.html")


def article_feed(request):
    return render(request, "article_feed.html")


def article(request):
    return render(request, "article.html")
