from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from website.models import Article
from .forms import ArticleForm

from traceback import print_exc
import re
import os


def get_imgs(html):
    pat = re.compile(r'<img [^>]*src="([^"]+)')
    imgs = pat.findall(html)
    return imgs


def delete_imgs(imgs):
    if imgs:
        base = os.getcwd()
        for img in imgs:
            try:
                img_path = os.path.join(base, img[1:])
                if os.path.exists(img_path):
                    os.remove(img_path)
            except Exception as e:
                print_exc(e)
                print(imgs)
                print(img_path)


def detail_article_view(request, slug):
    article = Article.objects.get(slug=slug)
    queryset = Article.objects.filter(fixed_to_top=False)
    if request.method == 'POST' and request.user.is_authenticated:
        if not article.fixed_to_top:

            # delete pics from media folder in case they were attached
            imgs = get_imgs(article.text)
            delete_imgs(imgs)

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
        "slug_id": slug
    }
    return render(request, "website/article_list.html", context)


class Article_Main_List_View(ListView):
    queryset = Article.objects.filter(fixed_to_top=False)


def create_article_view(request, slug="WS"):
    if request.method == 'POST':
        form = ArticleForm(request.POST, initial={'category': slug})
        if form.is_valid():
            form_data = form.cleaned_data
            a = Article.objects.create(**form_data)
            return redirect(a.get_absolute_url())
    else:
        form = ArticleForm(initial={'category': slug})
    return render(request, 'article_edit.html', {'form': form})


def edit_article_view(request, slug):
    article = Article.objects.get(slug=slug)
    start_imgs = get_imgs(article.text)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        print(form.cleaned_data)
        end_imgs = get_imgs(article.text)
        if set(start_imgs) != set(end_imgs):
            imgs = set(start_imgs) - set(end_imgs)
            delete_imgs(imgs)
        form.save()
        return redirect(article.get_absolute_url())

    context = {
        'form': form,
        'fixed': article.fixed_to_top,
        'edit': True,
        'link': article.get_absolute_url()
    }
    return render(request, 'article_edit.html', context=context)


def handler404(request, exception):
    response = render(request, "404.html")
    response.status_code = 404
    return response
