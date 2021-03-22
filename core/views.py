from django.shortcuts import render, HttpResponse
from core.models import *

# Create your views here.

# def homepage(request):
#     # return HttpResponse("<h2>Hello World</h2>")
#     return render(request, "index.html")

# def first_article(request):
#     article = Article.objects.first()
#     return render(
#         request, 
#         "article_page.html", 
#         {"article" : article}
#         )

def articles(request):
    articles = Article.objects.all()
    return render(
        request,
        "articles.html",
        {"articles" : articles}
    )

def authors(request):
    authors = Author.objects.all()
    return render(
        request,
        "authors.html",
        {"authors": authors}
        )

def article(request, id):
    article = Article.objects.get(id=id)
    return render(
        request,
        "article_page.html",
        {"article" : article }
        )

def about(request):
    return render(request, "about.html")