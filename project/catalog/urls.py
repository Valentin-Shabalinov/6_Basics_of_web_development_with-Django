from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import catalog_contacts, catalog_home, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    
    path('', catalog_home, name='home'),
    path('contacts/', catalog_contacts, name='contacts'),
    path('product/', ProductListView.as_view(), name='index'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='index_one'),
]
