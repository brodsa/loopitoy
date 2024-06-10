from django.shortcuts import render

from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView
    )

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from .models import Toys
from .forms import ToyForm

from django.contrib import messages

# Create your views here.

def all_toys(request):
    "A view to show all toys"

    toys = Toys.objects.all()
    context = {
        'toys': toys,
    }

    return render(request, 'toys/toys.html', context)


class AddToy(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    """ Add Toy View """
    template_name = 'toys/create_toy.html'
    model = Toys
    form_class = ToyForm

    def test_func(self):
        """ Test user with logged user otherwise 403 """
        return self.request.user.is_superuser
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        messages.success(
            self.request,
            'Successfully created book'
        )

        return super(AddToy, self).form_valid(form)
    
    # def get_success_url(self):
    #     """ Set up the books/key/id as success url"""
    #     return reverse_lazy('toys', kwargs={'pk': self.pk})