from django.db import models
from django.utils import timezone


NULLABLE = {"blank": True, "null": True}


class Product(models.Model):


    title = models.CharField(
        max_length=100, verbose_name="название", unique=True, **NULLABLE
    )
    description = models.TextField(unique=True, **NULLABLE)
    preview = models.ImageField(
        upload_to="product/", verbose_name="превью", **NULLABLE
    )
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    purchase_price = models.PositiveIntegerField(
        default=0, verbose_name="цена"
    )
    date_creation = models.DateTimeField(
        default=timezone.now, verbose_name="дата создания"
    )
    date_modified = models.DateTimeField(
        default=timezone.now, verbose_name="дата изменения"
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pk} {self.title} {self.purchase_price} {self.category}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"


class Category(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="название", **NULLABLE
    )
    description = models.TextField()

    def __str__(self):

        return self.title

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Version(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    version_number = models.PositiveIntegerField(
        default=0, verbose_name="номер версии"
    )
    version_name = models.CharField(
        max_length=100, verbose_name="название версии"
    )
    is_active_version = models.BooleanField(
        default=True, verbose_name="статус версии"
    )

    def __str__(self):
        return self.version_name

    class Meta:
        verbose_name = "версия"  
        verbose_name_plural = "версии"
