from django.urls import path
from newsletter.views import SubscribeToNewsletter

urlpatterns = [
    path("", SubscribeToNewsletter.as_view(), name="subscribe_to_newsletter"),
]