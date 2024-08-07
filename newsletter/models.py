from django.db import models


# Create your models here.
class Subscription(models.Model):
    """Model for Subscription"""

    email = models.EmailField(
        unique=True,
    )

    def __str__(self):
        return str(self.email)