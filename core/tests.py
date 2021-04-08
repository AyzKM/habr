from django.test import TestCase
from django.urls import reverse 
from core.models import Article
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
            article = Article()
            article.title = f'test title{i}'
            article.test = f'test text{i}'
            article.save()

        url = reverse('articles')
        response = self.client.get(url)
        self.assertIn('articles', response.context)

        articles = Article.objects.filter(is_active=True)
        self.assertEqual(articles.count(), n)
        for i in range (n):
            self.assertContains(response, article.title)
            self.assertContains(response, article.text)


