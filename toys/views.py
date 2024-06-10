from django.shortcuts import render

from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView
    )

from .models import Toys
from .forms import ToyForm

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

# Create your views here.

def all_toys(request):
    "A view to show all toys"

    toys = Toys.objects.all()
    context = {
        'toys': toys,
    }

    return render(request, 'toys/toys.html', context)


class AddToy(LoginRequiredMixin,CreateView):
    """ Add Toy View """
    template_name = 'toys/create_toy.html'
    model = Toys
    form_class = ToyForm