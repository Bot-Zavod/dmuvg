"""dmuvg_website URL Configuration

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

from dmuvg_website import settings
from website import views
from website.views import (
    ArticleDetailView,
    Article_Main_List_View
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Article_Main_List_View.as_view(), name="main_page"),
    path("news/", Article_Main_List_View.as_view(), name="news"),
    
    
    path("about/<slug:slug>", ArticleDetailView.as_view(), name="about"),
    path("article/<slug:slug>", ArticleDetailView.as_view(), name="article"),
    path("feed/<slug:slug>", views.article_list_view, name="feed"),
    path("feed/<slug:categ>/<slug:slug>", ArticleDetailView.as_view(), name="feed-article"),


    path("edit/<slug:slug>", views.edit_article_view, name="edit_page"),
    path("create/", views.create_article_view, name="new_page"),

    path("not_found/", views.not_found, name="error_page"),

    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT )
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

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
    # Еколого-просвітницькі заходи. {Раздел - лента}
    # Плани управління річковими басейнами. {Раздел - лента}
    # Інформація про оренду водних об'єктів. {статья}


# Робота басейнових рад. {статья}

# Запобігання корупції {статья}
