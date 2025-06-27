from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Optional booking status choices
BOOKING_STATUS = (
    ('Confirmed', 'Confirmed'),
    ('Cancelled', 'Cancelled'),
)

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.table_number} (Seats: {self.capacity})"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=10, choices=BOOKING_STATUS, default='Confirmed')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'time']
        unique_together = ('table', 'date', 'time')  # avoid double bookings

    def __str__(self):
        return f"{self.user.username} | {self.date} {self.time} | Guests: {self.guests}"


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image', blank=True)

    def __str__(self):
        return self.name
