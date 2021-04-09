import factory
from core.models import Article

class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article
    
    title = factory.Sequence(lambda n: f"My title number {n}")