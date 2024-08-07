from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ Class for User Profile """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_street_address': 'Street Address',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_county': 'County, State or Locality',
            'default_phone_number': 'Phone Number',
        }

        self.fields['default_street_address'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
            self.fields[field].widget.attrs['aria-label'] = field
