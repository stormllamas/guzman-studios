from django.db import models
from django.utils import timezone


class Transaction(models.Model):
    value = models.DecimalField(max_digits=30, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now, blank=True)
