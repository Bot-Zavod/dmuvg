from django.shortcuts import render, redirect, render_to_response
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from website.models import Article
from .forms import CreateArticleForm, EditArticleForm


class ArticleDetailView(DetailView):

    def get(self, request, slug):
        article = Article.objects.get(slug=slug)
        queryset = Article.objects.filter(fixed_to_top=False)
        context = {
            'object': article,
            'articles': queryset
        }
        return render(request, 'website/article_detail.html', context)


def article_list_view(request, slug, categ=None):
    queryset = Article.objects.filter(category=slug)
    context = {"objects_list": queryset}
    return render(request, "website/article_list.html", context)


class Article_Main_List_View(ListView):
    model = Article
    queryset = Article.objects.filter(fixed_to_top=False)


def create_article_view(request):

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


def edit_article_view(request, slug):
    model = Article
    article = Article.objects.get(slug=slug)
    # что такое slug? - генериует уникальную ссылку-название типо vodogospodarska-obstanovka
    # заработало?
    # no

    if request.method == "POST":
        print(str(request.POST))
        # form = EditArticleForm(
        #         data=request.POST or None,
        #         instance=article,
        #         # initial={
        #         #     'header': article.header,
        #         #     'text': article.text
        #         # },
        #     )

        form = EditArticleForm(data=request.POST)
        form.initial['header'] = article.header
        form.initial['text'] = article.text

        if form.is_valid():
            form.save()
    else:
        form = EditArticleForm()

    context = {'form': form}
    return render(request, 'article_edit.html', context)


def not_found(request):
    return render(request, "page_not_found.html")

