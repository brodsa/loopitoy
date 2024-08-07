from django.views.generic import (
    CreateView,
    TemplateView
    )
from django.contrib import messages

from .models import Contact
from .forms import ContactForm


class AddContact(CreateView):
    """ Send a contact message view """
    template_name = 'contact/contact.html'
    model = Contact
    form_class = ContactForm
    success_url = '/contact/thank_you'

class ThankYouContact(TemplateView):
    """ A class for Thank you for contacting us view """
    template_name = 'contact/thank_you.html'
