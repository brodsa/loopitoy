from django.shortcuts import (
    render,
    redirect,
    reverse
)

from django.db.models import Q

from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    UpdateView
    )

from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from .models import Toys
from .forms import ToyForm


# Create your views here.

def all_toys(request):
    "A view to show all toys"

    toys = Toys.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'You did not enter any search criteria!')
                return redirect(reverse('toys'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            toys = toys.filter(queries)


    context = {
        'toys': toys,
        'search_term': query
    }

    return render(request, 'toys/toys.html', context)


class AddToy(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    """ Add Toy View """
    template_name = 'toys/create_toy.html'
    model = Toys
    form_class = ToyForm
    success_url = '/toys/'


    def test_func(self):
        """ Test user with logged user otherwise 403 """
        return self.request.user.is_superuser
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        messages.success(
            self.request,
            'Successfully created toy'
        )

        return super(AddToy, self).form_valid(form)
    
    # def get_success_url(self):
    #     """ Set up the books/key/id as success url"""
    #     return reverse_lazy('toys', kwargs={'pk': self.pk})



class EditToy(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    """ Edit Toy View """
    template_name = 'toys/edit_toy.html'
    model = Toys
    form_class = ToyForm
    success_url = '/toys/'


    def test_func(self):
        """ Test user with logged user otherwise 403 """
        return self.request.user.is_superuser

    def form_valid(self, form):
        form.instance.user = self.request.user

        messages.success(
            self.request,
            'Successfully updated toy info'
        )

        return super(EditToy, self).form_valid(form)


class DeleteToy(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete toy view """
    model = Toys
    success_url = '/toys/'

    def test_func(self):
        """ Test user with superuser otherwise 403 """
        return self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        """ Display toast success on form submit """

        messages.success(
            self.request,
            'Successfully deleted toy'
        )
        return super().delete(request, *args, **kwargs)
    

class DetailToy(DetailView):
    """ Toy Detail View to see toy details """
    template_name = 'toys/toy_detail.html'
    model = Toys
    context_object_name = 'toy'
