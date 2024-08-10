from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from toys.models import Toys


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    sells = profile.sells.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'sells': sells,
        'profile': profile,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    if str(request.user) != str(order.user_profile):
        raise PermissionDenied("Permission denied.")

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def sell_history(request, sell_number):
    toy = get_object_or_404(Toys, number=sell_number)
    if str(request.user) != str(toy.user):
        raise PermissionDenied("Permission denied.")

    if toy.price is None:
        price, revenue, tax, to_pay = (0, 0, 0, 0)
    else:
        price = toy.new_price if toy.new_price else toy.price
        revenue = float(price)/2
        tax = round(revenue * 0.15, 2)
        to_pay = revenue - tax

    template = 'profiles/sell_history.html'
    context = {
        'sell': toy,
        'price': price,
        'revenue': revenue,
        'tax': tax,
        'to_pay': to_pay
    }

    return render(request, template, context)
