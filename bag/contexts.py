from decimal import Decimal

from django.shortcuts import get_object_or_404
from django.conf import settings

from toys.models import Toys


def bag_contents(request):
    """ Context processor of shopping bag to be available for all apps """

    bag_items = []
    total = 0
    bag = request.session.get('bag', {})
    product_count = 0

    for item_id, data in bag.items():
        toy = get_object_or_404(Toys, pk=item_id)
        total += toy.new_price if toy.new_price else toy.price
        bag_items.append({
                'item_id': item_id,
                'toy': toy,
        })
        product_count += 1

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY_FEE * product_count)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'delivery': delivery,
        'product_count': product_count,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
