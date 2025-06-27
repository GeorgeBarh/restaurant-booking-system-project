from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    class Meta:
        ordering = ['table_number']

    def __str__(self):
        return f"Table {self.table_number} (Seats {self.capacity})"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="bookings")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    class Meta:
        ordering = ['-date', 'time']

    def __str__(self):
        return f"{self.user} | {self.date} at {self.time} for {self.guests} guests"


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image', blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - ${self.price}"
