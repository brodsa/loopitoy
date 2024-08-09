from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404
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

from .models import Toys, Category
from profiles.models import UserProfile
from .forms import ToyForm


def all_toys(request):
    "A view to show all toys"

    toys = Toys.objects.filter(status__in=['eshop', 'in_bag'])
    categories = None
    age_groups = None
    query = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            toys = toys.filter(category__name__in=categories)
            categories_ls = toys.values_list('category', flat=True)
            categories = Category.objects.filter(pk__in=categories_ls)

        if 'age' in request.GET:
            age_groups = request.GET['age'].split(',')
            toys = toys.filter(age__in=age_groups)
            categories_ls = toys.values_list('category', flat=True)
            categories = Category.objects.filter(pk__in=categories_ls)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, 'You did not enter any search criteria!')
                return redirect(reverse('toys'))
            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            toys = toys.filter(queries)

    context = {
        'toys': toys,
        'search_term': query,
        'selected_categories': categories,
    }

    return render(request, 'toys/toys.html', context)


class AddToy(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """ Add Toy View """
    template_name = 'toys/create_toy.html'
    model = Toys
    form_class = ToyForm
    success_url = '/toys/'

    def test_func(self):
        """ Test user with logged user otherwise 403 """
        return self.request.user.is_superuser

    def form_valid(self, form):
        profile = get_object_or_404(UserProfile, user=self.request.user)
        form.instance.user_profile = profile

        messages.success(
            self.request,
            f'Successfully created toy {form.instance.name}.'
        )

        return super(AddToy, self).form_valid(form)


class EditToy(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Edit Toy View """
    template_name = 'toys/edit_toy.html'
    model = Toys
    form_class = ToyForm
    success_url = '/toys/'

    def test_func(self):
        """ Test user with logged user otherwise 403 """
        return self.request.user.is_superuser

    def form_valid(self, form):
        profile = get_object_or_404(UserProfile, user=self.request.user)
        form.instance.user_profile = profile

        messages.success(
            self.request,
            f'Successfully updated toy info of {form.instance.name}.'
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
            'Successfully deleted toy.'
        )
        return super().delete(request, *args, **kwargs)


class DetailToy(DetailView):
    """ Toy Detail View to see toy details """
    template_name = 'toys/toy_detail.html'
    model = Toys
    context_object_name = 'toy'


class SellToy(CreateView, LoginRequiredMixin):
    """ Sell Toy View """
    template_name = 'toys/sell_toy.html'
    model = Toys
    form_class = ToyForm
    success_url = '/toys/'

    def form_valid(self, form):

        messages.success(
            self.request,
            f'Successfully send toy for sell. The sell request is being proccessed. Check your profile for updates.'
        )

        return super(SellToy, self).form_valid(form)
