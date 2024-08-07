from django import forms
from .models import Subscription


class AddSubscription(forms.ModelForm):
    """Form for adding email to newsletter subscribers"""

    class Meta:
        """Meta class"""

        model = Subscription
        fields = [
            "email",
        ]

        widgets = {
            "email": forms.TextInput(attrs={"id": "newsletter_email"})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field.widget.attrs['label'] = "Enter email"
        