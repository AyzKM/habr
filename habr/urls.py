"""habr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from core.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign-in/', sign_in, name='sign-in'),
    path('sign-out/', sign_out, name='sign-out'),
    path('registration/', registration, name='registration'),
    path("", articles, name='articles'),
    path("authors/", authors, name='authors'),
    path("author/<int:pk>/", author_page, name="author"),
    path("article/<int:id>/", article_page, name='article'),
    path("about/", about, name="about"),
    path("article/<int:pk>/edit/", article_edit, name='article-edit'),
    path("add_article/", article_add, name='article-add'),
    path("arcticle/form", article_form, name='article-form'),
    path("article/<int:id>/delete", article_delete, name='article-delete'),
    path("article/<int:id>/hide", article_hide, name='article-hide'),
    path("search/", search, name='search'),
    path("top/", top, name="top"),
    path("test/", TestView.test_1, name="test"),

]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
