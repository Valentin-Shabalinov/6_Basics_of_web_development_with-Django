from django.urls import path

from catalog.views import catalog_contacts, catalog_home

app_name = 'catalog_contacts'

urlpatterns = [
    
    path('', catalog_home, name='home'),
    path('contacts/', catalog_contacts, name='contacts'),
]

