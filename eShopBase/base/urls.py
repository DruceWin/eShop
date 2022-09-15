from django.urls import path

from .views import basePage

app_name = "base"

urlpatterns = [
    path('', basePage, name='basePage'),
]