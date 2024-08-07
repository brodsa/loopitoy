from django.contrib import admin
from .models import Toys, Category, Brand


@admin.register(Toys)
class ToysAdmin(admin.ModelAdmin):
    """
    A Class to add and customize toys on admin panel
    """
    list_display = (
        'number',
        'name',
        'price',
        'new_price',
        'quality',
        'age',
        'category',
        'brand',
        'status',
        'user',
    )

    list_filter = ('status', 'user')
    search_fields = ('number',)
    readonly_fields = ['number']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    A Class to add and customize toys on admin panel
    """
    list_display = (
        'name',
        'friendly_name'
    )

    search_fields = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """
    A Class to add and customize toys on admin panel
    """
    list_display = (
        'name',
        'url'
    )

    search_fields = ('name',)
