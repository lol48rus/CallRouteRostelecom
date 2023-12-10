from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
import datetime
import random
# Create your models here.

class News:
    def __init__(self, title, text, state, date, author):
        self.title = title
        self.text = text
        self.state = state
        self.date = date
        self.author = author

    def __str__(self):
        return f'{self.title}: {self.text}, {self.state},{self.date}, {self.author}'

class Tag(models.Model):
    title = models.CharField(max_length=80)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', 'status']  #сортировка
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

#Менеджер модели
#Выбирает новости, созданные сегодня
import datetime
class PublishedToday(models.Manager):
    def get_queryset(self):
        return super(PublishedToday, self).get_queryset().filter(date__gte=datetime.date.today())

class Article(models.Model):
    categories = (('R', 'Report'),
                  ('DIVR', 'Dashboard/IVR'),
                  ('G', 'Global'),
                  ('C', 'CallRoute'),
                  )
    #поля
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField('Название', max_length=50, default='')
    anouncement = models.TextField('Аннотация', max_length=250)
    text = models.TextField('Текст новости')
    #дата создания новости
    date = models.DateTimeField('Дата публикации', auto_now=True) #auto_created=True
    #можно добавить дату изменения новости

    category = models.CharField(choices=categories, max_length=20, verbose_name='Категории')
    tags = models.ManyToManyField(to=Tag, blank=True)

    # status = models.BooleanField(default=True)
    slug = models.SlugField()

    #Использование менеджера моделей
    objects = models.Manager()
    published = PublishedToday()

    #методы моделей
    def __str__(self):
        return f'{self.title} от: {str(self.date)[:10]}'

    def get_absolute_url(self):
        return f'show/{self.id}'

    def tag_list(self):
        s = ''
        for t in self.tags.all():
            s+=t.title+''
        return s

    def shortdatestr(self):
        return f'{str(self.date)[:10]}'

    def shortanouncement(self):
        return f'{str(self.anouncement)[:25]}...'

    def generatecommentcount(self):
        return f'{str(random.randint(0,9))}'

    def image_tag(self):
        image = Image.objects.filter(article=self)
        print('image:', image)
        #image - хранит queryset
        #mark-safe - рендерит код на странице. помечает его безопасным для рендеринга
        if image:
            return mark_safe(f'<img src="{image[0].image.url}" height="50px" width="auto" />')
        else:
            return '(no image)'

    #метаданные модели
    class Meta:
        ordering = ['title', 'date']  #сортировка
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Image(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='article_images/') #лучше добавить поле default

    def __str__(self):
        return self.title

    def image_tag(self):
        #mark-safe - рендерит код на странице. помечает его безопасным для рендеринга
        if self.image is not None:
            return mark_safe(f'<img src="{self.image.url}" height="50px" width="auto" />')
        else:
            return '(no image)'


