from .models import Goods
from rest_framework import viewsets, permissions
from .serializers import GoodsSerializer


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    permissions_classess = [
         permissions.AllowAny
    ]
    serializer_class = GoodsSerializer
