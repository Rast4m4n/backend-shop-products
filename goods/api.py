from .models import *
from rest_framework import viewsets, permissions
from .serializers import *


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    permissions_classess = [
         permissions.AllowAny
    ]
    serializer_class = GoodsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permissions_classess = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_classess = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permissions_classess = [
        permissions.AllowAny
    ]
    serializer_class = OrderSerializer


class FavoriteGoodsViewSet(viewsets.ModelViewSet):
    queryset = FavoriteGoods.objects.all()
    permissions_classess = [
        permissions.AllowAny
    ]
    serializer_class = FavoriteGoodsSerializer