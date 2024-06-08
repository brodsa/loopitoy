from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


TOY_STATUS = [
    ('open', 'OPEN'),
    ('declaim', 'DECLAIM'),
    ('eshop', 'E-SHOP'),
    ('sold', 'SOLD'),
    ('paid', 'PAID')
]

AGE_CATEGORY = [
    ('newbor_infant', 'Newborn & Infant'),
    ('toodler', 'Toddler'),
    ('preschooler', 'Preschooler'),
    ('schooler', 'Schooler')
]

QUALITY = [
    ('new','New'),
    ('used_like_new', 'Used - Like New'),
    ('used_perfect', 'Used - Perfect'),
    ('used_good', 'Used - Good'),
    ('used_very_used', 'Used - Very Used')
]

class Category(models.Model):
    """A model to create and mange toys categories"""
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """Returns friendly name"""
        return self.friendly_name


class Toys(models.Model):
    """A model to create and manage toy products"""
    number = models.CharField(max_length=30)
    name = models.CharField(max_length=254, null=False, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    new_price = models.DecimalField(max_digits=6, decimal_places=2)
    quality = models.CharField(max_length=50, choices=QUALITY, default='open')
    age = models.CharField(max_length=50, choices=AGE_CATEGORY, default='open')
    category = models.ForeignKey(
        Category,
        related_name='toy_category',
        null=True, blank=True,
        on_delete=models.SET_NULL)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="media/books",
        force_format="WEBP",
        default='media/books/placeholder.placeholder.webp',
        blank=True
    )
    status = models.CharField(max_length=50, choices=TOY_STATUS, default='open')
    user = models.ForeignKey(
        User,
        related_name='toy_seller',
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on','status']

    def __str__(self):
        return str(self.name)
