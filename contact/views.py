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
    success_url = '/contact/home'

    def form_valid(self, form):
        """ Show a message if the form is valid """
        messages.success(
            self.request,
            'Thank you for contacting us, we have received your email.'
            )
        return super(AddContact, self).form_valid(form)
