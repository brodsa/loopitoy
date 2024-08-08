from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    """ A form to add review """

    class Meta:
        """ Define model, field, widget and labels"""
        model = Review

        fields = [
            'reviewer_name',
            'reviewer_email',
            'rating',
            'review',
            'want_replay',
        ]

         widgets = {
            "review": forms.Textarea(attrs={"cols": 3, "rows": 4}),
            "reviewer_name": forms.TextInput(attrs={'autofocus': True})
        }

        placeholder = {
            'reviewer_name': 'Name',
            'reviewer_email': 'Email'
            'rating': 'Select Rating Stars',
            'review': 'Write your review',
            'want_replay': 'Do you whish to be contacted back?'
        }