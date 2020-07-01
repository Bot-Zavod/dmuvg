from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from website.models import Article


# Главная {Главная}

# Про нас {дропДАУН}
# положення організації; {статья}
# інформація про керівництво; {статья}
# графік прийому громадян; {статья}
# структура організації; {статья}
# основні структурні підрозділи; {статья}
# контакти; {статья}
# підвідомчі організації; {статья}
# корисні посилання. {статья}


# Новини та анонси. {Раздел - лента}

# Інформація {дропДАУН}
# Водогосподарська обстановка. {Раздел - лента}
# Водні ресурси басейну річки. {статья}
# Роботу зі зверненнями громадян. {статья}
# Проведення еколого-просвітницьких заходів. {Раздел - лента}
# Плани управління річковими басейнами. {Раздел - лента}
# Інформація про оренду водних об'єктів. {статья}

# Робота басейнових рад. {статья}

# Запобігання корупції. {статья}


class ArticleDetailView(DetailView):
    model = Article


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        # self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Article.objects.filter(category=self.category)


def article_edit(request):
    article = Article.objects.get(pk=1)
    context = {"article": article}
    return render(request, "article_edit.html", context)


def not_found(request):
    return render(request, "page_not_found.html")
