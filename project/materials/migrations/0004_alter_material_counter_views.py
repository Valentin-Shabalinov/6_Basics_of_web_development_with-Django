# Generated by Django 4.2.5 on 2023-10-10 20:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("materials", "0003_alter_material_counter_views_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="material",
            name="counter_views",
            field=models.PositiveIntegerField(
                default=0, verbose_name="счетчик"
            ),
        ),
    ]
