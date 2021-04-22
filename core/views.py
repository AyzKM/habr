from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from core.models import *
from .forms import ArticleForm
from .filters import ArticleFilter

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('articles')

    return render(request, 'sign_in.html')

def sign_out(request):
    logout(request)
    return redirect(sign_in)

def registration(request):
    if request.method == "GET":
        return render(request, 'registr.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password != password2:
            return render(request, 'registr.html', {'message': 'passwords does not match!'})           
        elif User.objects.filter(username=username).exists():
           return render(request, 'registr.html', {'message': 'login is already used'})
        else:
            User.objects.create_user(
                username=username,
                password = password2
            )
            return redirect(sign_in)

def articles(request):
    article_filter = ArticleFilter(request.GET, queryset=Article.objects.filter(is_active=True))
    return render(
        request,
        "articles.html",
        {"article_filter" : article_filter}
    )

def authors(request):
    authors = Author.objects.all()
    return render(
        request,
        "authors.html",
        {"authors": authors}
        )

def author_page(request, pk):
    author = Author.objects.get(pk=pk)
    context = {
        "author": author,
        "user": author.user, 
    }
    return render(request, "author_page.html", context)

def article_page(request, id):
    article = Article.objects.get(id=id)
    article.views += 1
    if request.user.is_authenticated:
        article.readers.add(request.user)
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
    if not request.user == article.author.user:
        return HttpResponse('You do not have rights to edit')

    if request.method == "POST":
        article.title = request.POST.get("title")
        article.text = request.POST.get("text")
        article.save()
        return redirect(article_page, pk)
    return render(request, "article_edit.html", {"article": article})

@login_required(login_url='sign-in')
def article_add(request):
    if 'title' in request.POST and 'text' in request.POST: 
        title = request.POST["title"]
        text = request.POST["text"]
        picture = request.FILES.get("picture")
        article = Article(title=title, text=text, picture=picture)
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

def article_form(request):
    context = {}

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect(article_page, article.id)
    form = ArticleForm()
    context['form'] = form
    return render(request, 'form.html', context)

def is_author(user):
    if not user.is_authenticated:
         return False
    return Author.objects.filter(user=user).exists()


@user_passes_test(is_author)
def article_delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return HttpResponse("article succesfully has been deleted")


@permission_required('core.change_article')
def article_hide(request, id):
    article = Article.objects.get(id=id)
    article.is_active = False
    article.save()
    return redirect(articles)

def search(request):
    word = request.GET.get("word")
    articles = Article.objects.filter(
        Q(title__icontains=word) | Q(text__icontains=word),
        is_active=True
    ) #LIKE 
    return render(request, "search.html", {"articles":articles})

def top(request):
    articles = Article.objects.filter(is_active=True).order_by("-views")[:3]
    return render(request, "top.html", {"articles": articles})

class TestView:
     def test_1(self):
         return HttpResponse('test succeed!')
