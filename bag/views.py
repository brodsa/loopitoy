from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    reverse,
    HttpResponse
)
from django.contrib import messages

from toys.models import Toys

# Create your views here.

def view_bag(request):
    """A view that renders the shopping bag contents"""

    return render(request,'bag/bag.html')


def add_to_bag(request, item_id):
    """Add"""


    toy = get_object_or_404(Toys, pk=int(item_id))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})
    bag[item_id] = 1
    messages.success(request, f'Added {toy.name} to your bag')
    toy_sold = Toys.objects.get(pk = int(item_id))
    toy_sold.status = 'in_bag'
    toy_sold.save()
    
    request.session['bag'] = bag
    return redirect(redirect_url)