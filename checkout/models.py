import uuid
from decimal import Decimal

from django.db import models
from django.conf import settings
from django.db.models import Sum, Count

from django_countries.fields import CountryField

from toys.models import Toys
from profiles.models import UserProfile


class Order(models.Model):
    """A model for the order """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='orders'
        )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    street_address = models.CharField(max_length=80, null=False, blank=False)
    town_or_city = models.CharField(max_length=254, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
        )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
        )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
        )
    original_bag = models.TextField(
        null=False, blank=False, default=''
        )
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=''
        )

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        product_count = self.lineitems.aggregate(
            Count('lineitem_total'))['lineitem_total__count'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = Decimal(
                settings.STANDARD_DELIVERY_FEE * product_count)
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """ A model for the conent of the order """
    order = models.ForeignKey(
        Order,
        null=False, blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
        )
    toy = models.ForeignKey(
        Toys,
        null=False, blank=False,
        on_delete=models.CASCADE
        )
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
        )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        n_price = self.toy.new_price
        price = self.toy.price
        self.lineitem_total = n_price if n_price else price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.toy.number} on order {self.order.order_number}'
