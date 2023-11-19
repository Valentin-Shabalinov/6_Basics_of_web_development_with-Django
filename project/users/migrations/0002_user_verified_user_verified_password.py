# Generated by Django 4.2.5 on 2023-10-26 20:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="verified",
            field=models.BooleanField(
                blank=True, default=False, verbose_name="верифицирован"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="verified_password",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="ключ для верификации"
            ),
        ),
    ]
