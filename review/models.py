from django.db import models

# Create your models here.

RATING = [
    ('one', 1),
    ('two', 2),
    ('three', 3),
    ('four', 4),
    ('five', 5),
]

class Review(models.Model):
    """A model to create and manage toys brands"""
    reviewer_name = models.CharField(max_length=254)
    reviewer_email = models.EmailField(null=False, blank=False)
    rating = models.CharField(choices=RATING,max_length=150)
    review = models.TextField()
    want_replay = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.reviewer_name)
