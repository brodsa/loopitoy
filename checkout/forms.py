from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """ Class to Fill in Delivery Information """
    class Meta:
        model = Order
        fields = ('full_name', 'email',
                  'street_address',
                  'town_or_city', 'postcode',
                  'county', 'country',
                  'phone_number',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'street_address': 'Street Address ',
            'town_or_city': 'Town or City',
            'county': 'County, State or Locality',
            'postcode': 'Postal Code',
            'phone_number': 'Phone Number',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            css_style = 'stripe-style-input rounded-0'
            self.fields[field].widget.attrs['class'] = css_style
            self.fields[field].label = False
