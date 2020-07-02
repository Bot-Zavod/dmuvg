from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

from website.models import Article
from .forms import CreateArticleForm


class ArticleDetailView(DetailView):
    model = Article


def article_list_view(request, slug, categ=None):
    queryset = Article.objects.filter(category=slug)
    context = {"objects_list": queryset}
    return render(request, "website/article_list.html", context)


class Article_Main_List_View(ListView):
    model = Article
    queryset = Article.objects.filter(fixed_to_top=False)


def article_edit(request):

    if request.method == 'POST':
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            print(form_data)
            a = Article.objects.create(**form_data)
            return redirect(a.get_absolute_url())
    else:
        form = CreateArticleForm()
    return render(request, 'article_edit.html', {'form': form})

    # article = Article.objects.get(pk=1)
    # context = {"article": article}
    # return render(request, "article_edit.html", context)


def not_found(request):
    return render(request, "page_not_found.html")
