from django.urls import path
from .views import (
    view_bag,
    add_to_bag,
    remove_from_bag
)


urlpatterns = [
    path('', view_bag, name='view_bag'),
    path('add/<int:item_id>/', add_to_bag, name='add_to_bag'),
    path('remove/<int:item_id>/', remove_from_bag, name='remove_from_bag'),
]
