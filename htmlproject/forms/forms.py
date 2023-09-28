# forms.py
from django import forms

class SearchForm(forms.Form):
    max_value = forms.IntegerField(label="Maximum Value")
