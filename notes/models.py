from django.db import models

# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Note(MPTTModel):
    """
    Модель: Заметки
    """
    name = models.CharField('Название заметки', max_length=50)
    parent = TreeForeignKey('self', related_name='childs', null=True, blank=True, on_delete=models.SET_NULL,
                            verbose_name='Родительская заметка')
    text = models.TextField('Текст заметки')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.name

