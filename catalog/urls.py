from django.urls import path
from catalog.views import home, contacts
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts)
]
