from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    A Class to add and reviews
    """
    list_display = (
        'reviewer_name',
        'reviewer_email',
        'rating',
        'review',
        'want_replay',
        'approved'
    )

    search_fields = ('reviewer_name',)

