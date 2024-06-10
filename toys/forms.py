from django import forms

from .models import Toys


class ToyForm(forms.ModelForm):
    """A form to add Toy"""

    class Meta:
        """Define model, fields, widget and lables"""
        model = Toys

        fields = [
            'name',
            'description',
            'price',
            'new_price',
            'age',
            'quality',
            'image',
            'status',
        ]

        exclude = ('number','created_on')

        widgets = {
            "description": forms.Textarea(attrs={"cols": 3, "rows": 3}),
            "name": forms.TextInput(attrs={'autofocus': True})
        }

        placeholders = {
            'name': 'Toy Name *',
            'description': 'Provide information about toy, e.g. brand or material',
            'price': 'Price *',
            'new_price': 'New Price for discounts',
            'age': 'Select age category*',
            'quality': 'Select quality category*',
            'image': 'Upload toy image',
            'status': 'Toy status*',
        }


