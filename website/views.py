from django.shortcuts import render, redirect

from .models import Article, Category


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


def article_feed(request):
    return render(request, "article_feed.html")


def article(request):
    print(dict(request))
    article = Article.objects.filter(category__category_name='Робота басейнових рад')
    context = {'article': article[0]}
    return render(request, "article.html", context)


def article_edit(request):
    article = Article.objects.get(pk=1)
    context = {'article': article}
    return render(request, "article_edit.html", context)