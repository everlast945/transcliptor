from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from contents.filters import CategoryListFilter
from contents.models import Category
from contents.category.serializers import CategoryListSerializer


class CategoryListView(ListCreateAPIView):
    """
    Вью списка категорий
    """
    # permission_classes = (IsAuthenticated,)
    filterset_class = CategoryListFilter
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
