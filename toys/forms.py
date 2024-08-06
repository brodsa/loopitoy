from django import forms

from .models import Toys, Category


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
            'category',
            'image',
            'status',
        ]

        exclude = ('number', 'created_on')

        widgets = {
            "description": forms.Textarea(attrs={"cols": 3, "rows": 3}),
            "name": forms.TextInput(attrs={'autofocus': True})
        }

        placeholders = {
            'name': 'Toy Name *',
            'description':
                'Provide information about toy, e.g. brand or material',
            'price': 'Price *',
            'new_price': 'New Price for discounts',
            'age': 'Select age category*',
            'quality': 'Select quality category*',
            'category': 'Select toy category',
            'image': 'Upload toy image',
            'status': 'Toy status*',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # assign the category friendly names
        self.fields['category'].choices = friendly_names

        # give some css classes
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
