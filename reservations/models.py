from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()

    def __str__(self):
        return f"Table {self.number} ({self.seats} seats)"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Link to logged-in user
    name = models.CharField(max_length=100)  # still useful for display
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    guests = models.PositiveIntegerField(default=2)
    date = models.DateField()
    time = models.TimeField()
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.CharField(max_length=90,blank=True, null=True) 
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'time', 'table'], name='unique_table_booking')
        ]

    def __str__(self):
        return f"Booking for {self.name} on {self.date} at {self.time}"
