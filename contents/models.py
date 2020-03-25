from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from users.models import User


class Category(models.Model):
    """
    Модели категории
    """
    name = models.CharField('Наименование', max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Content(models.Model):
    """
    Модели контента
    """
    title = models.CharField('Тема', max_length=50)
    content = models.TextField('Контент')
    category = models.ForeignKey(Category, verbose_name='Категория', related_name='contents', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'

    def __str__(self):
        return self.title


class ContentMessage(models.Model):
    """
    Модель сообщения к контенту
    """
    content = models.ForeignKey(Content, verbose_name='Контент', related_name='messages', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Категория', related_name='messages', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Автор', related_name='content_messages', on_delete=models.CASCADE)

    text = models.TextField('Текст сообщения')
    datetime_created = models.DateTimeField('Дата-время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'{self.author}: {self.datetime_created}'


class TestCategory(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Тестовая категория'
        verbose_name_plural = 'Тестовые категории'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
