
# Обычные формы без привязки к модели
# from django import forms
#
# class UserForm(forms.Form):
#     login = forms.CharField(max_length=100,)
#     firstname = forms.CharField(max_length=100)
#     lastname = forms.CharField(max_length=100)
#     email = forms.EmailField(required=False)
#     password = forms.CharField(max_length=20)
#
#     message = forms.CharField(widget=forms.Textarea)


# Форма с привязкой к модели
from django import forms
from django.core.validators import MinLengthValidator
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple, Select
from .models import Account
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, FileInput, Select


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {'username': TextInput({'class': 'textinput form-control',
                                          'placeholder': 'username'}),
                   'email': EmailInput({'class': 'textinput form-control',
                                        'placeholder': 'email'}),
                   'first_name': TextInput({'class': 'textinput form-control',
                                            'placeholder': 'First name'}),
                   'last_name': TextInput({'class': 'textinput form-control',
                                           'placeholder': 'Last name'}),
                   }


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['nickname', 'gender']
        widgets = {'nickname': TextInput({'class': 'textinput form-control',
                                       'placeholder': 'nickname'}),
                   'gender': TextInput({'class': 'textinput form-control',
                                         'placeholder': 'gender'}),
                   }


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = {'user', 'nickname', 'gender'}
        widgets = {

        }