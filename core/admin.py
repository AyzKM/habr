from django.contrib import admin
from core.models import *

# Register your models here.
# admin.site.register(Article)
admin.site.register(Author)
admin.site.register(ArticleImage)

class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = Article

    list_display = ('title', 'author', 'is_active', 'updated_date')
    list_editable = ('author', 'is_active')
    ordering = ['-title']
    list_filter = ['is_active']
    search_fields = ['title', 'text']

    fields = ('title', 'text', 'views', 'created_date', 'updated_date', 'readers')
    readonly_fields = ('created_date', 'updated_date', 'readers')

admin.site.register(Article, ArticleAdmin)