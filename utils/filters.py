from django.db.models import Q
from django_filters.rest_framework import CharFilter, FilterSet


class SearchMixin(FilterSet):
    search_fields = ()
    q = CharFilter(method='filter_search')

    def filter_search(self, queryset, name, value):
        if value:
            q_objects = Q()
            for field in self.search_fields:
                q_objects |= Q(**{'{0}__{1}'.format(field, 'icontains'): value})
            queryset = queryset.filter(q_objects)
        return queryset.distinct()
