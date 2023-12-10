from django.shortcuts import render, HttpResponse, redirect, reverse
from django.urls import reverse_lazy
from .models import *
from django.db import connection, reset_queries
#Дженерик
from django.views.generic import DetailView, DeleteView, UpdateView
from .forms import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
# Create your views here.

#generic класс
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/generic_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_object = self.object
        images = Image.objects.filter(article=current_object)
        context['images'] = images
        return context

#generic класс
class ArticleUpdateView(UpdateView):
    model = Article
    success_url = reverse_lazy('news_index')
    template_name = 'news/update_article.html'
    fields = ['title', 'anouncement', 'text', 'tags', 'category']


# generic класс
class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('news_index')
    template_name = 'news/delete_news.html'



#@login_required(login_url=settings.LOGIN_URL)
def news(request):

    formArticle = ArticleForm()  # пустая форма

    #пример применения пользовательского менеджера
    # today_articles = Article.published.all()

    # title = 'Новости'
    #
    # n1 = News('News 1', 'Исправлен отчет "Показатели по скиллгруппе". Добавлены показатели LCR, SL за 20 сек, AVG.', 'danger', '07.11.23', 'User1')
    # n2 = News('News 2', 'Исправлена ошибка Telegram бота, при которой вовремя не отправлялись данные заказчику при показателе SL >= 80%. Исправлены мелкие недочеты.', 'info', '08.11.23', 'User2')
    # n3 = News('News 3', 'Добавлен Dashboard на страницу IVR. Внесены изменения для расчета показателя оценки качества обслуживания оператора', 'primary', '08.11.23', 'User3')
    # n4 = News('News 4', 'Text 4', 'warning', '09.11.23', 'User4')
    # news = [n1, n2, n3, n4]

    # article = Article.objects.all().first()
    # print('Автор новости', article.title, ':', article.author.account.gender)

    # print(request.user.id) #None - незарегистрированный ползователь
    # articles = Article.objects.filter(author=request.user.id)
    # print(articles)

    # articles = Article.objects.get(id=1)
    # print(articles.tags.all())
    #
    # tag = Tag.objects.filter(title='Crypto').first() #вместо first() можно [0]
    # tagged_news = Article.objects.filter(tags=tag)
    # print(tagged_news)
    #
    # article = Article.objects.filter(title__contains='Новость')
    # print('Filtered article:', article)
    #
    # context = {'news': news,
    #            'title': title,
    #            'article': articles
    #            }

    #Фильтр по авторам новостей
    # author_list = User.objects.all()
    # print(connection.queries)
    # print('author_list:', author_list)
    #
    # for author in author_list:
    #     print('author:', author)

    # Show Articles
    # selected = 0
    # articles = Article.objects.all()
    articles = Article.objects.all()
    selected_author = 0
    selected_category = 0

    author_list = User.objects.all()
    category_list = Article.categories

    # Новый обработчик
    if request.method == "POST":
        typename = request.POST.get('name')
        print('typename', typename)
        if typename == 'FilterApply': #фильтруем новости
            selected_author = int(request.POST.get('author_filter'))
            selected_category = int(request.POST.get('category_filter'))
            if selected_author == 0: #выбраны все авторы
                articles = Article.objects.all()
            else:
                articles = Article.objects.filter(author=selected_author)
            if selected_category != 0: #фильтруем найденные по авторам результаты по категориям
                articles = articles.filter(category__icontains=category_list[selected_category-1][0])
        elif typename == 'SaveArticle': #сохраняем статью
            form = ArticleForm(request.POST)
            if form.is_valid():
                current_user = request.user
                if current_user != None:  # проверка, что юзер не аноним
                    new_article = form.save(commit=False)  # чтобы не записывалась сразу в БД
                    new_article.author = current_user
                    new_article.save()  # сохраняем в БД
                    print(new_article.id)
                    try:
                        form.save_m2m()  # чтобы теги сохранились
                        messages.success(request, f'Article {new_article.title} created!')
                    except:
                        # Удаляем созданную новость
                        print('Новость удалена')

                    return redirect('news_index')  # Перенаправляем на страницу новостей
                    # form.save()
    else: #если страница открывается впервые
        selected_author = 0
        selected_category = 0
        articles = Article.objects.all()

    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     print('value:', request.POST.get('value'))
    #     print('name:', request.POST.get('name'))
    #     if name == 'SaveArticle':
    #         # Do something here.
    #         print('Methodname:', name)
    #     elif name == 'FilterApply':
    #         # Do something else here.
    #         print('Methodname:', name)
    #     elif name == 'Save':
    #         # Do something else here.
    #         print('Methodname:', name)
    #     else:
    #         print('Methodname:', name)
    # else:
    #     print('No Post method:')

    # Старый обработчик
    # if request.method == "POST":
    #     if name == 'FilterApply':
    #         print('Method name:', name)
    #         selected = int(request.POST.get('author_filter'))
    #         # category_selected = request.POST.get('category1')
    #         category_selected = [request.POST.get('category1'), request.POST.get('category2'), request.POST.get('category3'), request.POST.get('category4')]
    #
    #         print('category_selected:', category_selected)
    #         print('Count cat:', len(category_selected))
    #         if selected == 0:
    #             articles = Article.objects.all()
    #         # elif selected > 0 and len(category_selected) == 0:
    #         #      articles = Article.objects.filter(author=selected, category__in=category_selected)
    #         else:
    #             articles = Article.objects.filter(author=selected, category__in=category_selected)
    #     elif name == 'SaveArticle':
    #         form = ArticleForm(request.POST)
    #         if form.is_valid():
    #             current_user = request.user
    #             if current_user != None:  # проверка, что юзер не аноним
    #                 new_article = form.save(commit=False)  # чтобы не записывалась сразу в БД
    #                 new_article.author = current_user
    #                 new_article.save()  # сохраняем в БД
    #                 print(new_article.id)
    #                 try:
    #                     form.save_m2m()  # чтобы теги сохранились
    #                 except:
    #                     # Удаляем созданную новость
    #                     print('Новость удалена')
    #
    #                 context = {'Alert': 'Article +'
    #                            }
    #
    #                 return redirect('news_index')  # Перенаправляем на страницу новостей
    #                 # form.save()
    #     else:
    #         articles = Article.objects.all()
    # else:
    #     articles = Article.objects.all()

    # print('Автор новости', articles)
    # for articleone in articles:
        # print('category:', articleone.category)
        # print(articleone.date)
        #print(datetime.datetime.now() - articleone.date)
        #days_overdue = ExtractDay(timezone.now().date() - F('articleone.date'))

    # category_list = Article.objects.category.all()
    # print('category_list:', category_list)

    # article_model = Article
    # category_list = article_model.categories
    # print('categories:', category_list)

    # import datetime
    # print('Current DateTime:', datetime.datetime.now())
    #print(datetime.datetime.now() - articleone.date)

    # print(author_list)
    # print(request.name)

    # currentdatetime = datetime.datetime.now()

    context = {'articles': articles,
            'author_list': author_list,
            'category_list': category_list,
            'selected_author': selected_author,
            'selected_category': selected_category,
            'news': news,
            # 'today_articles': today_articles,
            # 'currentdatetime': currentdatetime,
            # 'mybirthdate': datetime.datetime(2004, 11, 18),
            # 'mydate': datetime.datetime(2020, 5, 17),
            'formArticle': formArticle
            }

    return render(request, 'news/news.html', context)

def detail(request,id):
    article = Article.objects.filter(id=id).first()
    print(article, type(article))

    #пример программного создания новости
    # author = User.objects.get(id=request.user.id)
    # article = Article(author=author, title='Заголовок 2', anouncement='Анонс', text='текст')
    # article.save()

    # articles = Article.objects.all()
    # s=''
    # for article in articles:
    #     s+= f'<h1>{article.title}</h1><br>'
    # return HttpResponse(s)

    context = {'article': article
               }
    return render(request, 'news/detail.html', context)

#только залогиненные пользователи. Редирект на главную страницу
#@login_required(login_url="/")
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES) #request.FILES - тут хранятся файлы
        if form.is_valid():
            current_user = request.user
            if current_user != None: #проверка, что юзер не аноним
                new_article = form.save(commit=False) #чтобы не записывалась сразу в БД
                new_article.author = current_user
                new_article.save() #сохраняем в БД
                print(new_article.id)

                #сохраним картинки
                for img in request.FILES.getlist('image_field'):
                    Image.objects.create(article=new_article, image=img, title=img.name)

                try:
                    form.save_m2m() #чтобы теги сохранились
                    messages.success(request, f'Article {new_article.title} created!')
                except:
                    #Удаляем созданную новость
                    print('Новость удалена')

                return redirect('news_index') #Перенаправляем на страницу новостей
                #form.save()
    else:
        form = ArticleForm() #пустая форма

    return render(request, 'news/create_article.html', {'form': form})
