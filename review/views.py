from django.shortcuts import render

from django.views.generic import (
    CreateView,
    ListView
    )

from django.contrib import messages

from .models import Review
from .forms import ReviewForm


class AddReview(CreateView):
    """ Add Review """
    template_name = 'review/review_add.html'
    model = Review
    form_class = ReviewForm
    success_url = '/review/about/'

    def form_valid(self, form):

        messages.success(
            self.request,
            f' Thank you for providing us with review.'
        )

        return super(AddReview, self).form_valid(form)


class Reviews(ListView):
    """ Display Reviews and about """
    template_name = 'review/about.html'
    model = Review
    context_object_name = 'reviews'