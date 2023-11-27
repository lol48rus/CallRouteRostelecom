from django.shortcuts import render, HttpResponse
from .models import *
from django.db import connection, reset_queries
# Create your views here.

def news(request):

    #пример применения пользовательского менеджера
    today_articles = Article.published.all()

    # title = 'Новости'
    #
    n1 = News('News 1', 'Исправлен отчет "Показатели по скиллгруппе". Добавлены показатели LCR, SL за 20 сек, AVG.', 'danger', '07.11.23', 'User1')
    n2 = News('News 2', 'Исправлена ошибка Telegram бота, при которой вовремя не отправлялись данные заказчику при показателе SL >= 80%. Исправлены мелкие недочеты.', 'info', '08.11.23', 'User2')
    n3 = News('News 3', 'Добавлен Dashboard на страницу IVR. Внесены изменения для расчета показателя оценки качества обслуживания оператора', 'primary', '08.11.23', 'User3')
    n4 = News('News 4', 'Text 4', 'warning', '09.11.23', 'User4')
    news = [n1, n2, n3, n4]

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
    author_list = User.objects.all()
    print(connection.queries)
    # print('author_list:', author_list)
    #
    # for author in author_list:
    #     print('author:', author)

    selected = 0
    if request.method=="POST":
        selected = int(request.POST.get('author_filter'))
        if selected == 0:
            articles = Article.objects.all()
        else:
            articles = Article.objects.filter(author=selected)
    else:
        articles = Article.objects.all()

    context={'articles': articles,
             'author_list': author_list,
             'selected': selected,
             'news': news,
             'today_articles': today_articles}

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

