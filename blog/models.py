from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=450) # заголовок поста
    author = models.ForeignKey('auth.User', # Автор поста, которого выбираем в административной панели управления
                               on_delete=models.CASCADE) # Удаление поста
    body = models.TextField(null=True, blank=True) # Поле нашего поста

    def __str__(self):
        return self.title
