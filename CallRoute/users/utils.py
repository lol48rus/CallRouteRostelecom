from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages

#декоратор
def check_group(*groups):
    def decorator(function):
        def wrapper(request, *args, **kwargs): #функция обертка
            print(groups)
            user = request.user
            #если есть группы у нашего пользвователя
            if user.groups.filter(name__in=groups):
                #то выполняем функцию
                return function(request, *args, **kwargs)
            messages.warning(request, 'Нет доступа')
            #пересылаем откуда пришел
            return HttpResponseRedirect(request.POST.get('next', '/'))
        return wrapper
    return decorator
