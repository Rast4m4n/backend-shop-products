from django.contrib import admin
from .models import Goods


class GoodsAdmin(admin.ModelAdmin):
    search_fields = ('id', 'nameGoods', 'priceGoods', 'category')
    list_filter = ('favoriteGoods',)


admin.site.register(Goods, GoodsAdmin)

