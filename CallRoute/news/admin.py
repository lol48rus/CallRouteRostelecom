from django.contrib import admin
from django.db.models.functions import Length
from django.db.models import Count
# Register your models here.
from .models import *


#Создадим пользовательский фильтр
class ArticleFilter(admin.SimpleListFilter):
    title = 'По длине новости'
    parameter_name = 'text'

    def lookups(self, request, model_admin):
        return [('S',("Короткие, < 5 знаков.")),
                ('M',("Короткие, 5-19 знаков.")),
                ('L',("Короткие, > 20 знаков.")),]

    #!!! Ругается на text_len !!!
    def queryset(self, request, queryset):
        if self.value() == 'S':
            return queryset.annotate(text_len=Length('text')).filter(text_len__lt <= 5) #аннотация + фильтр
        elif self.value() == 'M':
            return queryset.annotate(text_len=Length('text')).filter(text_len__lt >= 5, text_len__lt <= 19)  # аннотация + фильтр
        elif self.value() == 'L':
            return queryset.annotate(text_len=Length('text')).filter(text_len__lt >=20)  # аннотация + фильтр


#Отображение картинок на странице Новостей
class ArticleImageInline(admin.TabularInline): #StackedInline - тоже можно
    model = Image #выбираем модель, котору хотим привзять к Article
    extra = 3 #сколько доп полей картинок
    readonly_fields = ('id', 'image_tag')


class ArticleAdmin(admin.ModelAdmin):
    ordering = ['-date', 'title', 'author']
    list_display = ['title', 'author', 'date', 'symbol_count', 'image_tag', 'category']
    list_filter = ['date', ArticleFilter] #'title', 'author',
    list_display_links = ('title', 'date')

    #добавляем поле для поиска
    search_fields = ['title', 'tags__title'] # LookUp функцйии 'tags__title' - ищем по тегам, 'title__icontains' - поиск без учета регистра, title__startswith

    filter_horizontal = ['tags']

    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 5

    #добавляем поле с картинкой
    inlines = [ArticleImageInline]

    #редактируемые поля
    #list_editable = ['author']

    #заблокированные поля
    #readonly_fields = ['title', 'author']

    @admin.display(description='Длина', ordering='_symbols')
    def symbol_count(self, article: Article):
        return f"Символы: {len(article.text)}"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_symbols=Length('text'))
        return queryset


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'tag_count']
    list_filter = ['title', 'status']

    #регистрация пользовательских действий
    actions = ['set_true']

    @admin.display(description='Использований', ordering='tag_count')
    def tag_count(self, object):
        return object.tag_count #обращение к полю tag_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(tag_count=Count('article'))
        return queryset

    #@admin декоратор позволяет создавать свои действия
    @admin.action(description='Активировать выбранные теги')
    def set_true(self, request, queryset):
        amount = queryset.update(status=True) #пробегает по всему queryset и обновляет поле status
        self.message_user(request, f'Активировано {amount} тегов') #сообщение пользотваелю


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'article', 'image_tag']


@admin.register(ViewCount)
class ViewCountAdmin(admin.ModelAdmin):
    list_display = ['article', 'ip_address', 'view_date']

#регистрация моделей
admin.site.register(Article, ArticleAdmin)
#admin.site.register(Tag, TagAdmin)