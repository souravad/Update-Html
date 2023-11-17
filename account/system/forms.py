# forms.py
from django import forms
from .models import Product

class GenerateHTMLForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'