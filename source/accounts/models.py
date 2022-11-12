from django.db import models

# Create your models here.
from django.db.models import TextChoices
from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager

class Account(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True)

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars/',
        verbose_name='Аватар'
    )
    commented_posts = models.ManyToManyField(
        verbose_name='Прокомментированные публикации',
        to='topics.Topic',
        related_name='user_comments',
        blank=True
    )
    user_info = models.CharField(
        verbose_name='Информация о пользователе',
        null=True,
        blank=True,
        max_length=200
    )
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)
    is_deleted = models.BooleanField(verbose_name="Удалено", default=False, null=False)
    
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
