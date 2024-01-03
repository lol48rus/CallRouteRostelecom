from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    gender_choices= (('M', 'Male'),
                     ('F', 'Female'),
                     ('N/A', 'Not answered'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=100)
    birthdate = models.DateField(null=True)
    gender = models.CharField(choices=gender_choices, max_length=20)
    account_image = models.ImageField(default='default.jpg', upload_to='account_images') #pip install pillow в терминале для работы с изображениями

    def __str__(self):
        return f"{self.user.username}'s account"
    class Meta:
        ordering = ['user']  #сортировка
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


from news.models import Article
class FavoriteArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)