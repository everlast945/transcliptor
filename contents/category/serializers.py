from rest_framework import serializers

from contents.models import Category


class BaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class CategoryListSerializer(BaseCategorySerializer):
    pass
