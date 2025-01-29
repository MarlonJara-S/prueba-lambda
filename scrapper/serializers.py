from rest_framework import serializers
from .models import Product
from .models import Articulo

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'discount', 'seller', 'rating', 'image_url', 'product_url']


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'