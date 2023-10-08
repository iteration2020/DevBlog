from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100) # заголовок поста
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('auth.User', # Автор поста, которого выбираем в административной панели управления
                               on_delete=models.CASCADE) # Удаление поста
    body = models.TextField(null=True, blank=True) # Поле нашего поста

    def __str__(self):
        return self.title
