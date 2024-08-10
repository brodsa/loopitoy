from django.urls import path
from .views import profile, order_history, sell_history

urlpatterns = [
    path('', profile, name='profile'),
    path('order_history/<order_number>', order_history, name='order_history'),
    path('sell_history/<sell_number>', sell_history, name='sell_history'),
]
