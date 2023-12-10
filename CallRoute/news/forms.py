from django import forms
from django.core.validators import MinLengthValidator
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple, Select, CheckboxInput, RadioSelect
from .models import Article

#Для работы с несколькими файлами
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


#Для работы с несколькими файлами
class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


#Форма создания новости
class ArticleForm(ModelForm):
    #поле картинки (1 файл)
    image_field = MultipleFileField() #или forms.ImageField()
    class Meta:
        model = Article
        fields = ['title', 'anouncement', 'text', 'tags', 'author', 'category']
        widgets = {
            'anouncement': Textarea(attrs={'cols': 80, 'rows':2}),
            'text': Textarea(attrs={'cols': 80, 'rows': 2}), #'style':'width:30%' - можно назначить стайл, класс
            'tags': CheckboxSelectMultiple(),
            'category': RadioSelect()
            #'author': Select()
        }