from django import forms
from .models import City

class Cityform(forms.ModelForm):
    class Meta:
        model = City
        exclude = ('slug',)


class Searchform(forms.Form):
    search_field = forms.CharField(max_length=50, required=True)
