"""Forms of the project."""
from unittest.util import _MAX_LENGTH
from django import forms

class ThingForm(forms.Form):
    name = forms.CharField(label = "Your name",max_length=50)
    description = forms.CharField(widget=forms.Textarea())
    quantity = forms.CharField(label ="Quantity", widget=forms.NumberInput())
# Create your forms here.
