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
                  'quantity_in_stock')
        model = Product
