from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from contents.models import Content
from contents.serializers import ContentSerializer


class ContentView(RetrieveUpdateDestroyAPIView):
    """
    Вью списка категорий
    """
    # permission_classes = (IsAuthenticated,)
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
