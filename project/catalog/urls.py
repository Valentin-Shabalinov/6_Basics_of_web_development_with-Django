from django.urls import path, include
from catalog.views import (
    contacts,
    ProductListView,
    ProductDetailView,
    MerchandiseListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    toggle_activity,
)

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
    path("", ProductListView.as_view(), name="index"),
    path("contacts", contacts, name="contacts"),
    path("merchandise", MerchandiseListView.as_view(), name="merchandise"),
    path("create/", ProductCreateView.as_view(), name="create_product"),
    path(
        "update/<int:pk>/", ProductUpdateView.as_view(), name="update_product"
    ),
    path("<int:pk>/view/", ProductDetailView.as_view(), name="view_product"),
    path(
        "delete/<int:pk>/", ProductDeleteView.as_view(), name="delete_product"
    ),
    path("activity/<int:pk>/", toggle_activity, name="toggle_activity"),
]
