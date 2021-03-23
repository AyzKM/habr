from django.shortcuts import render, HttpResponse, redirect
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

def article_page(request, id):
    article = Article.objects.get(id=id)
    article.views += 1
    article.save()
    return render(
        request,
        "article_page.html",
        {"article" : article }
        )

def about(request):
    return render(request, "about.html")

def article_edit(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == "POST":
        article.title = request.POST.get("title")
        article.text = request.POST.get("text")
        article.save()
        return redirect(article_page, pk)
    return render(request, "article_edit.html", {"article": article})

def article_add(request):
    if 'title' in request.POST and 'text' in request.POST: 
        title = request.POST["title"]
        text = request.POST["text"]
        article = Article(title=title, text=text)
        article.save()
        return redirect(articles)
    return render(
        request, 
        "article_add.html", 
        )


