from rest_framework import serializers

from contents.category.serializers import BaseCategorySerializer
from contents.models import Content, ContentMessage
from users.serializers import BaseUserSerializer


class BaseMessageSerializer(serializers.ModelSerializer):
    author = BaseUserSerializer()

    class Meta:
        model = ContentMessage
        fields = ('author', 'text', 'datetime_created')


class ContentSerializer(serializers.ModelSerializer):
    category = BaseCategorySerializer()
    messages = BaseMessageSerializer(many=True)

    class Meta:
        model = Content
        fields = ('title', 'content', 'category', 'messages')
