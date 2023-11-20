from django.contrib import admin
from catalog.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name",)
    search_fields = ("name", "description")


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("id", "country", "inn", "address")


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "version_number",
        "version_name",
        "is_active",
    )
    list_filter = ("product",)
    search_fields = ("product", "version_number")
