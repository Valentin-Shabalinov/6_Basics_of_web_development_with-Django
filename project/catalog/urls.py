from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import catalog_contacts, catalog_home, index, index_one

app_name = CatalogConfig.name

urlpatterns = [
    
    path('', catalog_home, name='home'),
    path('contacts/', catalog_contacts, name='contacts'),
    path('product/', index, name='index'),
    path('<int:pk>/product/', index_one, name='index_one'),
]
