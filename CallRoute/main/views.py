from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from django.utils import translation
from django.conf import settings
from .models import News
from .forms import *

def index(request):
    title = 'Главная страница'

    context = {'title': title
               }

    return render(request, 'main/index.html', context)

def login(request):
    title = 'Авторизация'

    context = {'title': title
               }

    if request.method == 'POST':
        print ('Получили post-запрос')
        print(request.POST)
        loginname = request.POST.get('loginname')
        password = request.POST.get('password')
    else:
        print('Получили get-запрос')

    return render(request, 'main/login.html', context)

def register(request):
    title = 'Регистрация'

    context = {'title': title
               }

    return render(request, 'main/register.html', context)

def profile(request):
    title = 'Профиль'

    context = {'title': title
               }

    return render(request, 'main/profile.html', context)

# def news(request):
#     return render(request, 'main/news.html')

def news(request):

    title = 'Новости'

    n1 = News('News 1', 'Исправлен отчет "Показатели по скиллгруппе". Добавлены показатели LCR, SL за 20 сек, AVG.', 'danger', '07.11.23', 'User1')
    n2 = News('News 2', 'Исправлена ошибка Telegram бота, при которой вовремя не отправлялись данные заказчику при показателе SL >= 80%. Исправлены мелкие недочеты.', 'info', '08.11.23', 'User2')
    n3 = News('News 3', 'Добавлен Dashboard на страницу IVR. Внесены изменения для расчета показателя оценки качества обслуживания оператора', 'primary', '08.11.23', 'User3')
    n4 = News('News 4', 'Text 4', 'warning', '09.11.23', 'User4')
    news = [n1, n2, n3, n4]

    context = {'news': news,
               'title': title
               }

    return render(request, 'main/news.html', context)

def get_news(request, a):
    return HttpResponse(f'Вы ввели: {a}')

def faq(request):

    if request.method == 'POST':
        print ('Получили post-запрос')
        # print(request.POST)
        form = ContactForm(request.POST)
        # form.name = request.POST['name']
        if form.is_valid():
            print('Сообщение отправлено', form.cleaned_data) #очищенные данные после проверки
        else:
            print(form.errors)

        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # message = request.POST.get('message')
    else:
        print('Получили get-запрос')
        form = ContactForm()
        # form.name='Любимый клиент'

    title = 'FAQ'

    context = {'title': title,
               'form': form
               }

    return render(request, 'main/faq.html', context)

def reports(request):
    title = 'Reports'

    context = {'title': title
               }

    return render(request, 'main/reports.html')

def custom_404(request, exception):
    #return render(request, 'main/404.html')
    return HttpResponse(f'404 ошибка:{exception}' )

def index_test(request):
    return render(request, 'main/index_test.html')

def blank(request):
    return render(request, 'main/blank.html')



def selectlanguage(request):
    #в 25 символов входит корневой каталог + код языка из двух букв
    print('Начало работы выбор языка')
    url = request.META.get('HTTP_REFERER')[25:]
    #print(request.META)
    print('URL:', url)
    if request.method == 'POST':
        current_language = translation.get_language()
        print('До:', current_language)
        lang = request.POST.get('language')
        translation.activate(lang)
        print('После:', translation.get_language())
        response = HttpResponse('')
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
        print('/' + lang + '/' + url)
        print('Сработал выбор языка')
        return HttpResponseRedirect('/' + lang + '/' + url)


def language_redirect(request):
    return redirect('home')