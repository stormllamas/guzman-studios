from django.urls import path
from .api import TransactionAPI

urlpatterns = [
    path("<int:pk>", TransactionAPI.as_view(), name="transaction")
]
