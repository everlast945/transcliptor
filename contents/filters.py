from django_filters.rest_framework import FilterSet

from utils.filters import SearchMixin


class CategoryListFilter(SearchMixin, FilterSet):
    search_fields = ('name', )
