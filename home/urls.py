from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    Index,
    HowItWorks,
    PrivacyPolicy
)


urlpatterns = [
    path('', Index.as_view(),name='home'),
    path('how-it-works', HowItWorks.as_view(),name='how'),
    path('privacy-policy', PrivacyPolicy.as_view(),name='privacy'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)