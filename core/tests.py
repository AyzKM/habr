from django.test import TestCase
from django.urls import reverse 
from .models import Article
from .factories import ArticleFactory, UserFactory
# Create your tests here.

class HomepageTestCase(TestCase):
    def test_homepage_loads_success(self):
        url = reverse('articles')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '10')

    def test_homepage_with_articles_success(self):        
        n = 3
        for i in range(n):
            article = ArticleFactory()

        article.is_active = False
        article.save()

        url = reverse('articles')
        response = self.client.get(url)
        self.assertIn('articles', response.context)
        articles = Article.objects.filter(is_active=True)
        self.assertEqual(articles.count(), n - 1)

        for article in articles:
            self.assertContains(response, article.title)
            self.assertContains(response, article.text)

class loginTestCase(TestCase):
    def test_login_success(self):
        user = UserFactory()
        url = reverse('sign-in')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)