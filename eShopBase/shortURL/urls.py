from django.urls import path

from .views import short_url, MakeShortURL

app_name = "shortURL"

urlpatterns = [
    path('make_short_url/', MakeShortURL.as_view(), name='make_short_url'),
]
