from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404
)
from django.contrib import messages
from django.conf import settings

import json
import stripe

from .forms import OrderForm
from .models import Order, OrderLineItem
from toys.models import Toys
from bag.contexts import bag_contents

# Create your views here.

def checkout(request):
    print('checkout')
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    print(stripe_public_key)
    print(stripe_secret_key)

    if request.method == 'POST':
        print('method-post')
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address': request.POST['street_address'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            print('form-valid')
            order = order_form.save(commit=False)
            print(bag.items())
            for item_id, item_data in bag.items():
                try:
                    toy = Toys.objects.get(id=item_id)
                    print(toy)
                    order_line_item = OrderLineItem(
                        order=order,
                        toy=toy
                    )
                    order_line_item.save()
                except Toys.DoesNotExist:
                    messages.error(request, (
                        "One of the toys in your bag wasn't found in our database. "
                        "Please contact us!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            print('redirect')
            return redirect(reverse('checkout_success', args=[order.order_number]))
        
        else:
            print('form-valid not')
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        print('request GET')
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('toys'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )
        order_form = OrderForm()
        
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
    
    
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)



def checkout_success(request, order_number):
    """
    A View to manage successful checkouts
    """
    print('checkout_success')
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    # remove bag as the order is successfully proceede and update toy status
    if 'bag' in request.session:
        print('bag')
        bag = request.session.get('bag', {})
        for item_id, item_data in bag.items():
            toy_sold = Toys.objects.get(pk = int(item_id))
            print(toy_sold)
            toy_sold.status = 'sold'
            toy_sold.save()

        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
