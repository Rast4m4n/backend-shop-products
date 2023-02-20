from django.db import models


class Goods(models.Model):
    nameGoods = models.CharField(max_length=100)
    compositionOfGoods = models.TextField()
    weightGoods = models.CharField(max_length=10)
    pathImage = models.TextField(null=True)
    priceGoods = models.IntegerField()
    favoriteGoods = models.BooleanField(default=False)
    category = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nameGoods} {self.priceGoods}₽ {self.weightGoods} грамм'

    class Meta:
        verbose_name = "Goods"
        verbose_name_plural = "Goods"
