from django.urls import path

from .views import(
    all_toys,
    AddToy,
)

urlpatterns = [
    path('', all_toys, name='toys'),
    path('add/',AddToy.as_view(),name='add_toy' ),
]
