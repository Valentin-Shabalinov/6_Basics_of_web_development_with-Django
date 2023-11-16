# Generated by Django 4.2.6 on 2023-11-14 03:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                unique=True,
                verbose_name="Наименование",
            ),
        ),
    ]
