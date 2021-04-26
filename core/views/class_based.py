from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DeleteView

from core.models import *
from core.mixins import IsAuthorMixin


class DeleteArticleView(LoginRequiredMixin, IsAuthorMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        article = Article.objects.get(id=kwargs["id"])
        article.delete()
        return HttpResponse("article succesfully has been deleted")

class TopView(LoginRequiredMixin, ListView):
    queryset = Article.objects.filter(is_active=True).order_by("-views")[:3]
    template_name = 'top.html'

class TestView(TemplateView):
    template_name = 'test.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test1'] = 'bla bla bla'
        return context