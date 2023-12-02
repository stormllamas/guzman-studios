from django.utils import timezone
from django.db import models
import datetime


class Booking(models.Model):
    price = models.DecimalField(max_digits=30, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f'{self.id} - {datetime.datetime.strftime(self.creation_date, "%d/%m/%Y")}'
