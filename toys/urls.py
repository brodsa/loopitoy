from django.urls import path

from .views import(
    all_toys,
    AddToy,
    EditToy,
    DeleteToy
)

urlpatterns = [
    path('', all_toys, name='toys'),
    path('add/',AddToy.as_view(),name='add_toy' ),
    path('edit/<slug:pk>/',EditToy.as_view(),name='edit_toy' ),
    path('delete/<slug:pk>/', DeleteToy.as_view(), name='delete_toy'),
]
