from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        print('вошли в register')
        form = UserCreationForm(request.POST)
        # print(form)
        if form.is_valid():
            print('форма валид')
            user = form.save() #появляется новый юзер

            category = request.POST['account_type']
            if category == 'author':
                group = Group.objects.get(name='Actions Required')
                user.groups.add(group)
            else:
                group = Group.objects.get(name='Reader')
                user.groups.add(group)

            # group = Group.objects.get(name='Authors')
            # user.groups.add(group)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            account = Account.objects.create(user=user, nickname=user.username)
            # account.save()

            print(form.cleaned_data)
            user_auth = authenticate(username=username, password=password)
            if user_auth is not None:
                login(request, user_auth)
                messages.success(request, f'{username} registered!')
                return redirect('home')
            else:
                print(user_auth)

    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


def register_custom(request):
    print('вошли в register_custom')
    if request.POST == 'POST':
        form = CustomUserCreationForm()
        print(form)
        if form.is_valid():
            print('форма валид')
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)

# if request.method == 'POST':
#         print('вошли в register')
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             print('форма валид')
#             user = form.save() #появляется новый юзер
#             group = Group.objects.get(name='Authors')
#             user.groups.add(group)
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             authenticate(username=username, password=authenticate)
#             messages.success(request, f'{username} registered!')
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     context = {'form': form}
#     return render(request, 'users/register.html', context)


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

    user_list = User.objects.all()
    print(user_list)

    context = {'form': form,
               'user_list': user_list}
    return render(request, 'users/users.html', context)

def profile(request):
    title = 'Профиль'

    context = {'title': title
               }

    return render(request, 'users/profile.html', context)


from .forms import AccountUpdateForm, UserUpdateForm
from .utils import check_group #импорт декоратора
@check_group('Authors',)
def profile_update(request):
    user = request.user
    account = Account.objects.get(user=user)
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        account_form = AccountUpdateForm(request.POST, request.FILES, instance=account)
        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            messages.success(request,"Профиль успешно обновлен")
            return redirect('profile')
    else:
        context = {'account_form':AccountUpdateForm(instance=account),
                   'user_form':UserUpdateForm(instance=user)}
    return render(request,'users/edit_profile.html',context)