from django.db import models
from django.utils import timezone

# Create your models here.


class Material(models.Model):
    title = models.CharField(max_length=100, verbose_name="название")
    slug = models.CharField(
        max_length=100, verbose_name="slug", null=True, blank=True
    )
    body = models.TextField(verbose_name="описание")
    preview = models.ImageField(
        upload_to="product/", null=True, blank=True, verbose_name="превью"
    )
    date_creation = models.DateTimeField(
        default=timezone.now, verbose_name="дата"
    )
    published = models.BooleanField(default=True, verbose_name="статус")
    counter_views = models.PositiveIntegerField(
        default=0, verbose_name="счетчик"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "материал"
        verbose_name_plural = "материалы"
