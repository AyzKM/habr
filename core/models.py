from django.db import models
from datetime import datetime

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title