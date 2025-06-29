from django.db import models
from django.contrib.auth.models import User

from django.db import models



class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()

    def __str__(self):
        return f"Table {self.number} ({self.seats} seats)"

class Booking(models.Model):
    name = models.CharField(max_length=100)  # required
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)  # required
    date = models.DateField()
    time = models.TimeField()
    table = models.ForeignKey('Table', on_delete=models.SET_NULL, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'time', 'table'], name='unique_table_booking')
        ]

    def __str__(self):
        return f"Booking for {self.name} on {self.date} at {self.time}"



