from django.urls import path
from .api import BookingAPI

urlpatterns = [
    path("<int:pk>", BookingAPI.as_view(), name="booking")
]
