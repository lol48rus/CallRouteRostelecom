from django.shortcuts import render, HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):

    # if request.method == 'POST':
    #     print ('Получили post-запрос')
    #     print(request.POST)
    #     form = UserForm(request.POST)
    #     # form.name = request.POST['name']
    #     if form.is_valid():
    #         print('Сообщение отправлено', form.cleaned_data) #очищенные данные после проверки
    #     else:
    #         print(form.errors)
    #
    #     # name = request.POST.get('name')
    #     # email = request.POST.get('email')
    #     # message = request.POST.get('message')
    # else:
    #     print('Получили get-запрос')
    #     form = UserForm()
    #     # form.name='Любимый клиент'
    #
    # context = {'form': form
    #            }

    # return render(request, 'users/users.html', context)

    if request.method == 'POST':
        print('Получили post-запрос')
        print(request.POST)
        form = AccountForm(request.POST)
        # form.name = request.POST['name']
        if form.is_valid():
            print('Сообщение отправлено', form.cleaned_data) #очищенные данные после проверки
            form.save()
        else:
            print(form.errors)

        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # message = request.POST.get('message')
    else:
        print('Получили get-запрос')
        form = AccountForm()
        # form.name='Любимый клиент'

    context = {'form': form}
    return render(request, 'users/users.html', context)

