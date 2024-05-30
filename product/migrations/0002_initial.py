# Generated by Django 5.0.3 on 2024-05-29 23:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("product", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="shoes",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AddField(
            model_name="shoes",
            name="collection",
            field=models.ManyToManyField(
                max_length=40,
                related_name="collection_product",
                to="product.collectionproduct",
                verbose_name="Коллекция",
            ),
        ),
        migrations.AddField(
            model_name="shoes",
            name="color",
            field=models.ManyToManyField(
                max_length=40,
                related_name="color_product",
                to="product.colorproduct",
                verbose_name="Цвет обуви",
            ),
        ),
        migrations.AddField(
            model_name="shoes",
            name="country_of_manufacture",
            field=models.ManyToManyField(
                blank=True,
                max_length=10,
                related_name="country_of_manufacture_product",
                to="product.countryofmanufacture",
                verbose_name="Страна производитель",
            ),
        ),
        migrations.AddField(
            model_name="shoes",
            name="gender",
            field=models.ManyToManyField(
                blank=True,
                max_length=40,
                related_name="gender",
                to="product.gender",
                verbose_name="Пол",
            ),
        ),
        migrations.AddField(
            model_name="shoes",
            name="insole_material",
            field=models.ManyToManyField(
                max_length=50,
                related_name="insole_material_product",
                to="product.insolematerialproduct",
                verbose_name="Материал стельки",
            ),
        ),
        migrations.AddField(
            model_name="shoes",
            name="lining_material",
            field=models.ManyToManyField(
                max_length=50,
                related_name="lining_material_product",
                to="product.liningmaterialproduct",
                verbose_name="Материал подкладки",
            ),
        ),
        migrations.AddField(
            model_name="shoes",
            name="outsole_material",
            field=models.ManyToManyField(
                max_length=50,
                related_name="outsole_material_product",
                to="product.outsolematerialproduct",
                verbose_name="Материал подошвы",
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="shoes",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="product.shoes",
                verbose_name="Комментарий",
            ),
        ),
        migrations.AddField(
            model_name="rating",
            name="shoes",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="product.shoes",
                verbose_name="обувь",
            ),
        ),
        migrations.AddField(
            model_name="shoes",
            name="size",
            field=models.ManyToManyField(
                max_length=40,
                related_name="size_product",
                to="product.sizeproduct",
                verbose_name="Размер обуви",
            ),
        ),
        migrations.AddField(
            model_name="shoes",
            name="upper_material",
            field=models.ManyToManyField(
                max_length=75,
                related_name="upper_material_product",
                to="product.uppermaterialproduct",
                verbose_name="Материал верха",
            ),
        ),
    ]