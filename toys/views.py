from django.shortcuts import render

from .models import Toys

# Create your views here.

def all_toys(request):
    "A view to show all toys"

    toys = Toys.objects.all()
    context = {
        'toys': toys,
    }

    return render(request, 'toys.html', context)
