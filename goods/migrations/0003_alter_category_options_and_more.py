# Generated by Django 4.1.3 on 2023-03-14 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("goods", "0002_category_user_alter_goods_options_order_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "categories"},
        ),
        migrations.RenameField(
            model_name="category",
            old_name="name",
            new_name="categoryName",
        ),
        migrations.RemoveField(
            model_name="goods",
            name="favoriteGoods",
        ),
    ]
