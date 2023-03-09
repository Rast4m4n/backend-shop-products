from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'categories'


class Goods(models.Model):
    nameGoods = models.CharField(max_length=100)
    compositionOfGoods = models.TextField()
    weightGoods = models.CharField(max_length=10)
    pathImage = models.TextField(null=True)
    priceGoods = models.IntegerField()
    favoriteGoods = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nameGoods} {self.priceGoods}₽ {self.weightGoods} грамм'

    class Meta:
        verbose_name = "Goods"
        verbose_name_plural = "Goods"


class User(models.Model):
    phoneNumber = models.CharField(max_length=11, null=False)
    name = models.CharField(max_length=100, null=True)
    mail = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=100, null=True)
    entrance = models.CharField(max_length=2, null=True) # подъезд
    floor = models.CharField(max_length=2, null=True)
    flat = models.CharField(max_length=3, null=True)

    def __str__(self):
        return f'{self.phoneNumber} {self.name}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    countOfGoods = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        return f'{self.user} {self.goods} {self.time}'


class FavoriteGoods(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    isFavorite = models.BooleanField(null=False)

    def __str__(self):
        return f'{self.user} {self.goods} {self.isFavorite}'

    class Meta:
        verbose_name_plural = 'Favorite Goods'
