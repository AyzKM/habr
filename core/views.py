from django.shortcuts import render, HttpResponse, redirect
from core.models import *

def articles(request):
    articles = Article.objects.filter(is_active=True)
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
        user = request.user

        if not Author.objects.filter(user=user).exists():
            author = Author(user=user, nickname=user.username)
            author.save()

        author = request.user.author
        article.author = author
        article.save()
        return redirect(articles)
    return render(
        request, 
        "article_add.html", 
        )


def article_delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return HttpResponse("article succesfully has been deleted")

def article_hide(request, id):
    article = Article.objects.get(id=id)
    article.is_active = False
    article.save()
    return redirect(articles)

def search(request):
    word = request.GET.get("word")
    articles = Article.objects.filter(title__contains=word, is_active=True) #LIKE 
    return render(request, "articles.html", {"articles":articles})