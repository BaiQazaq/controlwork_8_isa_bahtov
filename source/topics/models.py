from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models


class Topic(models.Model):
    title = models.CharField(verbose_name='Название', null=False, blank=False, max_length=200)
    description = models.CharField(verbose_name='Описание', null=False, blank=False, max_length=200)
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='topics', null=False, blank=False,
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)
    is_deleted = models.BooleanField(verbose_name="Удалено", default=False, null=False)


class Comment(models.Model):
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='comments', null=False,
                               blank=False,
                               on_delete=models.CASCADE)
    topic = models.ForeignKey(verbose_name='Публикация', to='topics.Topic', related_name='comments', null=False,
                             blank=False, on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Текст', null=False, blank=False, max_length=200)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)
    is_deleted = models.BooleanField(verbose_name="Удалено", default=False, null=False)
    
    def __str__(self):
        return self.text[:150]


