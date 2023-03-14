from django.contrib import admin
from .models import *


class GoodsAdmin(admin.ModelAdmin):
    search_fields = ('id', 'nameGoods', 'priceGoods', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('id', 'categoryName',)


class UserAdmin(admin.ModelAdmin):
    search_fields = ('id', 'phoneNumber', 'name', 'mail')
    list_filter = ('id', 'name',)


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Order)
admin.site.register(FavoriteGoods)

