from django import forms

from .models import ModelShortURL


class UrlForm(forms.ModelForm):
    class Meta:
        model = ModelShortURL
        fields = ['long_URL']
