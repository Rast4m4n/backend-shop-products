from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/goods', GoodsViewSet, 'goods')
router.register('api/categories', CategoryViewSet, 'categories')
router.register('api/users', UserViewSet, 'users')
router.register('api/favorites', FavoriteGoodsViewSet, 'favorites')
router.register('api/orders', OrderViewSet, 'orders')

urlpatterns = router.urls
