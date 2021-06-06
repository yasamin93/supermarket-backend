from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'barcode',
                  'name',
                  'category',
                  'description',
                  'unit_cost',
                  'quantity_in_stock',
                  'creator')
        model = Product


class UserSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'url')

    def get_url(self, obj):
        return f'http://127.0.0.1:8000/api/v1/users/{obj.id}'
