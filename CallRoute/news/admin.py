from django.contrib import admin
from django.db.models.functions import Length
from django.db.models import Count
# Register your models here.
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    ordering = ['-date', 'title', 'author']
    list_display = ['title', 'author', 'date', 'symbol_count']
    list_filter = ['title', 'author', 'date']
    list_display_links = ('title', 'date')

    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 5

    #редактируемые поля
    #list_editable = ['author']

    #заблокированные поля
    #readonly_fields = ['title', 'author']

    @admin.display(description='Длина', ordering='_symbols')
    def symbol_count(self, article:Article):
        return f"Символы: {len(article.text)}"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_symbols=Length('text'))
        return queryset

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'tag_count']
    list_filter = ['title', 'status']

    @admin.display(description='Использований', ordering='tag_count')
    def tag_count(self, object):
        return object.tag_count #обращение к полю tag_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(tag_count=Count('article'))
        return queryset

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'article', 'image_tag']

#регистрация моделей
admin.site.register(Article, ArticleAdmin)
#admin.site.register(Tag, TagAdmin)