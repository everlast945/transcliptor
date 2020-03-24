from django.urls import path

from contents.category.views import CategoryListView

app_name = 'category'

urlpatterns = [
    path('', CategoryListView.as_view(), name='list'),
]