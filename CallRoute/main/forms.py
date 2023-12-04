from django import forms
from .validators import russian_email
from django.core.validators import MinLengthValidator

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           validators=[MinLengthValidator(2)],
                           initial='Имя')
    email = forms.EmailField(validators=[russian_email])
    message = forms.CharField(widget=forms.Textarea) #disabled=True
    demo = forms.BooleanField(required=False,
                              help_text='Подсказка',
                              label='Демо поле',
                              initial=True)