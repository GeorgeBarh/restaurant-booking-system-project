from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number} (Seats: {self.capacity})"


class Booking(models.Model):
    STATUS_CHOICES = (
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Confirmed')

    class Meta:
        unique_together = ('table', 'date', 'time')
        ordering = ['date', 'time']

    def __str__(self):
        return f"{self.user.username} | {self.date} {self.time} | Guests: {self.guests}"


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image', blank=True)

    def __str__(self):
        return self.name