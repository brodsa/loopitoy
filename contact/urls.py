from django.urls import path, include

from .views import AddContact


urlpatterns = [
    path('', AddContact.as_view(), name='contact'),
    path('home', include('home.urls'), name='home'),
]
