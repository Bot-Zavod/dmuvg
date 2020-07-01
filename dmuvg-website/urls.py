"""dmuvg-website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from website import views
from website.views import (
            ArticleDetailView,
            ArticleListView
)



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

# about
#     position of the organization
#     management information
#     reception schedule
#     structure of the organization
#     main structural units
#     contacts
#     subordinate organizations
#     useful links

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


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", ArticleListView.as_view(), name="main_page"),
    path("about/<slug:slug>", ArticleDetailView.as_view(), name="about"),
    path("article/<slug:slug>", ArticleDetailView.as_view(), name="article"),

    path("edit/", views.article_edit, name="edit_page"),
    path("new_article/", views.article_edit, name="new_page"),
    
    path("not_found/", views.not_found, name="error_page"),
]
