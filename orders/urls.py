from django.urls import path
from .views import Order

urlpatterns = [
    path('', Order.as_view(), name='order'),
]