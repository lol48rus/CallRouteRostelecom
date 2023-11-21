from django.db import models

# Create your models here.

class News:
    def __init__(self,title,text,state,date,author):
        self.title = title
        self.text = text
        self.state = state
        self.date = date
        self.author = author

    def __str__(self):
        return f'{self.title}: {self.text}, {self.state},{self.date}, {self.author}'