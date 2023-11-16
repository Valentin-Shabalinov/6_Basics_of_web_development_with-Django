# Generated by Django 4.2.6 on 2023-11-16 17:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0003_version"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "категория", "verbose_name_plural": "категории"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "продукт", "verbose_name_plural": "продукты"},
        ),
        migrations.RemoveField(
            model_name="category",
            name="name",
        ),
        migrations.RemoveField(
            model_name="product",
            name="date_of_creation",
        ),
        migrations.RemoveField(
            model_name="product",
            name="image",
        ),
        migrations.RemoveField(
            model_name="product",
            name="last_modified_date",
        ),
        migrations.RemoveField(
            model_name="product",
            name="name",
        ),
        migrations.AddField(
            model_name="category",
            name="title",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="название"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="date_creation",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="дата создания"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="date_modified",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="дата изменения"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="product",
            name="preview",
            field=models.ImageField(
                blank=True, null=True, upload_to="product/", verbose_name="превью"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="title",
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                unique=True,
                verbose_name="название",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="purchase_price",
            field=models.PositiveIntegerField(default=0, verbose_name="цена"),
        ),
    ]
