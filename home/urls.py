from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    Index,
    HowItWorks,
    PrivacyPolicy,
    ReturnAndRefund,
    TermsAndConditions,
)


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('how-it-works', HowItWorks.as_view(), name='how'),
    path('privacy-policy', PrivacyPolicy.as_view(), name='privacy'),
    path('return-and-refund', ReturnAndRefund.as_view(), name='return'),
    path('terms-and-conditions', TermsAndConditions.as_view(), name='terms'),
]
