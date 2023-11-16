# Generated by Django 4.2.6 on 2023-11-16 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_alter_product_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
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
                (
                    "version_number",
                    models.PositiveIntegerField(default=0, verbose_name="номер версии"),
                ),
                (
                    "version_name",
                    models.CharField(max_length=100, verbose_name="название версии"),
                ),
                (
                    "is_active_version",
                    models.BooleanField(default=True, verbose_name="статус версии"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "версия",
                "verbose_name_plural": "версии",
            },
        ),
    ]
