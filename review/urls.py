from django.urls import path

from .views import AddReview, Reviews

urlpatterns = [
    path('', Reviews.as_view(), name='about'),
    path('add/', AddReview.as_view(), name='add_review'),
   
]
