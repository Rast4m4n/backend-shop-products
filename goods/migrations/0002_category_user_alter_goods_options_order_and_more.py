# Generated by Django 4.1.3 on 2023-03-09 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("goods", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phoneNumber", models.CharField(max_length=11)),
                ("name", models.CharField(max_length=100, null=True)),
                ("mail", models.CharField(max_length=100, null=True)),
                ("street", models.CharField(max_length=100, null=True)),
                ("entrance", models.CharField(max_length=2, null=True)),
                ("floor", models.CharField(max_length=2, null=True)),
                ("flat", models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name="goods",
            options={"verbose_name": "Goods", "verbose_name_plural": "Goods"},
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("countOfGoods", models.IntegerField()),
                ("time", models.DateTimeField()),
                (
                    "goods",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="goods.goods"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="goods.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FavoriteGoods",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isFavorite", models.BooleanField()),
                (
                    "goods",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="goods.goods"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="goods.user"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Favorite Goods",
            },
        ),
        migrations.AlterField(
            model_name="goods",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="goods.category"
            ),
        ),
    ]
