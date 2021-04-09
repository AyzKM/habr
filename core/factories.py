import factory
from core.models import Article

class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article
    