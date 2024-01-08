
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


# Кастомная форма регистрации
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form


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
                   'first_name': TextInput({'class': 'textinput form-control',
                                            'placeholder': 'First name'}),
                   'last_name': TextInput({'class': 'textinput form-control',
                                           'placeholder': 'Last name'}),
                   'account_image': FileInput({'class': 'form-control',
                                       'placeholder': 'image'})
                   }


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = {'user', 'nickname', 'gender'}
        widgets = {

        }


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user