from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'categoryName')


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        category_representation = representation.pop('category')
        representation['categoryName'] = category_representation['categoryName']
        return representation


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FavoriteGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteGoods
        fields = '__all__'
