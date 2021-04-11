from django.contrib.auth.models import User
import factory
from core.models import Article

class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article
    
    title = factory.Sequence(lambda n: f"My title number {n}")

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    
    username = factory.Sequence(lambda n: f"testuser{n}")
    password = factory.PostGenerationMethodCall('set_password', 'test1234')