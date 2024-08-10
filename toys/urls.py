from django.urls import path

from .views import (
    all_toys,
    AddToy,
    EditToy,
    DeleteToy,
    DetailToy,
    SellToy,
)

urlpatterns = [
    path('', all_toys, name='toys'),
    path('add/', AddToy.as_view(), name='add_toy'),
    path('edit/<slug:pk>/', EditToy.as_view(), name='edit_toy'),
    path('delete/<slug:pk>/', DeleteToy.as_view(), name='delete_toy'),
    path('detail/<slug:pk>/', DetailToy.as_view(), name='toy_detail'),
    path('sell/', SellToy.as_view(), name='sell_toy'),
]
