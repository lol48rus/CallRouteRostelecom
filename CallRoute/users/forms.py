
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


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = {'user', 'nickname', 'gender'}
        widgets = {

        }