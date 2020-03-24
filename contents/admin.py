from django.contrib import admin

from contents.models import Category, Content, ContentMessage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')


@admin.register(ContentMessage)
class ContentMessageAdmin(admin.ModelAdmin):
    list_display = ('content', 'category', 'author')
