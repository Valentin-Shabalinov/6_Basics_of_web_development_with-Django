# Generated by Django 4.2.6 on 2023-10-28 20:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0002_remove_post_number_of_views_post_count_views_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date_of_creation",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Дата создания"
            ),
        ),
    ]
