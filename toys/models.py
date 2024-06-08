import random
import string

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
    
    class Meta:
        verbose_name_plural = 'Categories'

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
    quality = models.CharField(max_length=50, choices=QUALITY, default='used_good')
    age = models.CharField(max_length=50, choices=AGE_CATEGORY, default='newborn_infant')
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
        verbose_name_plural = 'Toys'

    def __str__(self):
        return str(self.name)
    

    def save(self, *args, **kwargs):
        print(self.id)

        if self.id is None: 
            last_toy = Toys.objects.order_by('id').last().id #get the last record that has the same combination.
            print(last_toy)

            id_seed = 0
            if last_toy is None:
                id_seed = 0
            else:
                id_seed = int(last_toy)

            random.seed(id_seed)
            chars = string.ascii_letters + string.digits
            chars_selected = "".join(random.choices(chars, k=10))
            self.number = f"PP-{chars_selected[:4]}-{chars_selected[4:-2]}-{chars_selected[-2:]}"
        else:
            self.number = self.number

        super(Toys, self).save(*args, **kwargs)
